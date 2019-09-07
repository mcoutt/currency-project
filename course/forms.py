from django import forms


class CurrencyForm(forms.Form):
    currency_name_first = forms.CharField(label='Currency first name', max_length=10)

