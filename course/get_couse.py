import requests
from bs4 import BeautifulSoup as bs
import time
from currency.celery import app
from course.models import Course


def get_course(cur_name='usd'):
    soup = requests.get(f'https://ru.cryptonator.com/rates/convert/?amount=1&primary=btc&secondary={cur_name}&source=liverates').text
    soup = bs(soup, 'html.parser')
    tags = str(soup.find_all('h2', class_='heading-large'))
    get_num = tags.split('<strong>')[1].split('\t')[12]
    return get_num


@app.task()
def save_currency_data():
    while True:
        get_value = get_course()
        save_btc = Course.objects.create(currency_name='BTC', currency_value=get_value)
        save_btc.save()
        time.sleep(10)


if __name__ == '__main__':
    save_currency_data()
