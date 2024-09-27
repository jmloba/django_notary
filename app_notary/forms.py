from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Notarized_Documents, Notary_Category


class Notary_Categoryform(forms.ModelForm):
  class Meta:
    model=Notary_Category
    fields=["doc_category"]


class Notary_form(forms.ModelForm):
  class Meta:
    model=Notarized_Documents

    fields=["category","firstname","lastname","bookno", "pageno", "recordno", "amount"]

    '''
    fields=["category","firstname", "lastname","bookno", "pageno", "recordno", "myfile", "myimage","amount"]
    '''

class Notary_form_A(forms.ModelForm):
  class Meta:
    model=Notarized_Documents

 
    fields=["category","firstname", "lastname","bookno", "pageno", "recordno", "myfile", "myimage","amount"]

    
