from django import forms 
from app_expenses.models import Expense

class Expense_Form (forms.ModelForm):
  class Meta :
    model= Expense

    fields=('description','date','amount','category')


class UpdateRecord_ExpenseForm(forms.ModelForm):
  class Meta :
    model= Expense
    fields=('date','description','amount','posted',)
    labels={
      'date':'Date',
      'description':'Description',
      'amount':'Amount',
      'posted':'Posted',
      
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecord_ExpenseForm,self).__init__(*args,**kwargs)
    self.fields['date'].required=True
    self.fields['description'].required=True
    self.fields['amount'].required=True 

class DeleteRecord_ExpenseForm(forms.ModelForm):
  class Meta :
    model= Expense
    fields=('date','description','amount','posted',)
    labels={
      'date':'Date',
      'description':'Description',
      'amount':'Amount',
      'posted':'Posted',
      
    }
  def __init__(self,*args,**kwargs):
    super(DeleteRecord_ExpenseForm,self).__init__(*args,**kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['date'].widget.attrs['readonly'] = True
      self.fields['description'].widget.attrs['readonly'] = True
      self.fields['amount'].widget.attrs['readonly'] = True     
      self.fields['posted'].widget.attrs['readonly'] = True     