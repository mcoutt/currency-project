from currency.celery import app
from course.models import Course, Currency
from celery.schedules import crontab
from celery.task import periodic_task
from datetime import timedelta
from course.get_couse import get_currencies, get_course, get_course_json


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, save_currency_data, name='add every 10')


@app.task()
def save_currency_data():
    get_course_json()


@app.task()
def save_another_currency_data(another_currency):
    get_course_json(cur_to=another_currency.lower())


@periodic_task(run_every=timedelta(seconds=7))
def set_schedule(another_currency=None):
    get_db_currencies = Course.objects.values_list('currency_target').distinct()
    another_currency = [i[0] for i in get_db_currencies]

    get_course_json(cur_to=another_currency.lower())


# @app.task()
# @periodic_task(run_every=crontab(seconds=3, minute=0, hour=0))
# def set_schedule(args):
#     app.conf.beat_schedule = {
#         "see-you-in-ten-seconds-task": {
#             "task": "course.get_course.save_another_currency_data",
#             "schedule": 3.0,
#             "args": args
#         }
#     }


# @app.on_after_configure.connect
# def add_periodic(another_currency, **kwargs):
#     app.add_periodic_task(3.0, save_another_currency_data(another_currency), name='add every 10')
