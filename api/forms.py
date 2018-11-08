from django import forms


class DetailsForm(forms.Form):
    username = forms.CharField(label='url', max_length=100)

