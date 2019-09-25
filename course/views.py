from django.shortcuts import render
from django.db.models import F, Q
from django.http import Http404
from course.models import Course, Currency
from course.get_couse import get_currencies, get_course_json
from course.tasks import save_currency_data, set_schedule, save_another_currency_data


def get_init():
    _get_currencies = Currency.objects.get_queryset()
    if _get_currencies.__len__() == 0:
        get_currencies()
    get_course = Course.objects.get_queryset()
    if get_course.__len__() == 0:
        get_course_json()


def index(request):
    try:
        get_init()
        from .forms import CurrencyForm
        save_currency_data.delay()

        if request.method == 'GET':
            form = CurrencyForm()
            get_another = Course.objects.values('currency_base', 'currency_target__name', 'currency_value',
                                                'created_date').distinct('currency_target')
            context = {'another_currency': get_another}

            return render(request, 'index.html', {'context': context, 'form': form})

        elif request.method == 'POST':
            form = CurrencyForm(request.POST)
            id_another_currency = form.data.get('currency_name_first')
            another_currency = Currency.objects.filter(id=id_another_currency).first()
            get_data = get_course_json(cur_to=another_currency.code)
            get_another = Course.objects.values_list('currency_target').distinct()
            if get_data.get('success'):
                set_schedule.delay(another_currency.code)
                another_currency = [Course.objects.filter(currency_target=i[0]).order_by('-created_date').first() for i
                                    in get_another]
                context = {'another_currency': another_currency}
            elif get_data.get('error'):
                another_currency = [Course.objects.filter(currency_target=i[0]).order_by('-created_date').first() for i
                                    in get_another]
                context = {'another_currency': another_currency,
                           'error': get_data.get('error')}
            return render(request, 'index.html', {'context': context, 'form': form})

    except Exception as e:
        print(e)
        return Http404
