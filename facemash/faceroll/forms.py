# forms.py
from django import forms

class SearchForm(forms.Form):
  roll_no = forms.CharField()
