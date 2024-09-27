from django import forms 
from app_accounting.models  import chart_acct

from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

class CreateAcctMasterForm(forms.ModelForm):
  class Meta :
    model = chart_acct
    fields=('chrt_accno','chrt_desc','chrt_H_D','beg_bal',)
    labels={
      'chrt_accno':'Account NO:',
      'chrt_desc':'Description:',
      'chrt_H_D':'Header/Detail',
      'beg_bal':'Beginning Balance',
    }
  def __init__(self,*args,**kwargs):
    super(CreateAcctMasterForm,self).__init__(*args,**kwargs)
    self.fields['chrt_accno'].required=True  
    self.fields['chrt_desc'].required=True      
    self.fields['chrt_H_D'].required=True          
    self.fields['beg_bal'].required=True       

class UpdateRecordChrtMastForm(forms.ModelForm):
  class Meta :
    model = chart_acct
    fields=('chrt_accno','chrt_desc','chrt_H_D','beg_bal',)
    labels={
      'chrt_accno':'Account NO:',
      'chrt_desc':'Description:',
      'chrt_H_D':'Header/Detail',
      'beg_bal':'Beginning Balance',
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecordChrtMastForm,self).__init__(*args,**kwargs)    
    self.fields['chrt_accno'].required=True  
    self.fields['chrt_desc'].required=True      
    self.fields['chrt_H_D'].required=True          
    self.fields['beg_bal'].required=True        


class DeleteRecordChrtMastForm(forms.ModelForm):
  class Meta :
    model = chart_acct
    fields=('chrt_accno','chrt_desc','chrt_H_D','beg_bal',)
    labels={
      'chrt_accno':'Account NO:',
      'chrt_desc':'Description:',
      'chrt_H_D':'Header/Detail',
      'beg_bal':'Beginning Balance',
    }
  def __init__(self,*args,**kwargs):
    super(DeleteRecordChrtMastForm,self).__init__(*args,**kwargs)    
    self.fields['chrt_accno'].disabled=True
    self.fields['chrt_desc'].disabled=True      
    self.fields['chrt_H_D'].required=True          
    self.fields['beg_bal'].required=True            