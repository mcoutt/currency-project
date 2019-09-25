from django import forms
from course.models import Currency, Course
from django.db import utils


def get_currencies():
    try:
        get_courses = Currency.objects.all()
        return [(i.id, i.name) for i in get_courses]
    except utils.OperationalError:
        return ['BTC',]


class CurrencyForm(forms.Form):
    currency_name_first = forms.ChoiceField(widget=forms.Select, choices=get_currencies())

