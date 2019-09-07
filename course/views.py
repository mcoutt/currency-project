from django.shortcuts import render
from django.http import Http404
from course.models import Course
from course.get_couse import get_course
from .forms import CurrencyForm


def index(request):
    try:
        get_value = Course.objects.filter(currency_name='USD').order_by('-created_date').first()

        if request.method == 'GET':
            form = CurrencyForm()
            get_another = Course.objects.values_list('currency_name').distinct()
            another_currency = [Course.objects.filter(currency_name=i[0]).order_by('-created_date').first() for i in get_another]
            context = {'BTC': get_value, 'another_currency': another_currency}

            return render(request, 'index.html', {'context': context, 'form': form})
        elif request.method == 'POST':
            form = CurrencyForm(request.POST)
            another_currency = form.data.get('currency_name_first')
            get_another_currency = get_course(another_currency)

            data = Course.objects.create(currency_name=another_currency.upper(), currency_value=get_another_currency)
            data.save()

            get_another = Course.objects.values_list('currency_name').distinct()
            another_currency = [Course.objects.filter(currency_name=i[0]).order_by('-created_date').first() for i in get_another]

            context = {'BTC': get_value, 'another_currency': another_currency}
            return render(request, 'index.html', {'context': context, 'form': form})
    except Exception as e:
        print(e)
        return Http404
