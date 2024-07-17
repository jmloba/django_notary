from django import forms
from django.forms import ModelForm
from app_notary.models import Notarized_Documents, Notary_Category



class Notary_form(forms.ModelForm):
  class Meta:
    model=Notarized_Documents

    fields=["category","firstname", "lastname","amount_paid","bookno", "pageno", "recordno", "myfile", "myimage",]
  
    '''
    fields=["category","firstname", "lastname","amount_paid","bookno", "pageno", "recordno", "myfile", "myimage",]

    
    fields=["category","firstname", "amount_paid", "myimage",]
    '''