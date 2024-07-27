
from django import forms 

class SearchForm (forms.Form):
  invoiceno = forms.IntegerField()
  