import requests
from bs4 import BeautifulSoup as bs
from course.models import Course, Currency


def get_course_json(cur_from='btc', cur_to='usd'):
    try:
        get_data = requests.get(f'https://api.cryptonator.com/api/ticker/{cur_from}-{cur_to.lower()}').json()
        if get_data.get('success'):
            price = get_data.get('ticker').get('price')
            base = get_data.get('ticker').get('base')
            target = get_data.get('ticker').get('target') if cur_to != 'usd' else 'US Dollar'
            _base = base if Currency.objects.filter(name=base).__len__() > 0 else 'BTC'
            target = Currency.objects.filter(code=target).first()
            if target:
                to_save = {'currency_base': _base, 'currency_target': target, 'currency_value': price}
                course = Course.objects.create(**to_save)
                course.save()
                return get_data
        elif get_data.get('error').__len__() > 0:
            return get_data
    except Exception as e:
        print(e)


def get_currencies():
    try:
        curr_list = requests.get('https://www.cryptonator.com/api/currencies').json()
        rows = curr_list.get('rows')
        for one_currency in rows:
            to_save = {'name': one_currency.get('name'), 'code': one_currency.get('code'), 'statuses': one_currency.get('statuses')[0]}
            currency = Currency.objects.create(**to_save)
            currency.save()
    except Exception as e:
        print('get currencies Exception: ', e)

def get_course(cur_name='usd'):
    soup = requests.get(f'https://ru.cryptonator.com/rates/convert/?amount=1&primary=btc&secondary={cur_name}&source=liverates').text
    soup = bs(soup, 'html.parser')
    tags = str(soup.find_all('h2', class_='heading-large'))
    get_num = tags.split('<strong>')[1].split('\t')[12]
    return get_num
