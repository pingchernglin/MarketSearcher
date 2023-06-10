from django import forms

class TimeFilterForm(forms.Form):
    filter_time = forms.CharField(max_length=100)

class AddressFilterForm(forms.Form):
    filter_address = forms.CharField(max_length=100)