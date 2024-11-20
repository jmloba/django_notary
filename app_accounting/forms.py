from django import forms
from django.db.models.base import Model 
from app_accounting.models  import chart_acct, myvalidator,voucher_creation
# for testing
from app_accounting.models  import CreateVoucherGroup

from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from django.core.validators import RegexValidator


numeric_char = RegexValidator(r"^[0-9]+$", 'only numbers are allowed')

alphanumeric = RegexValidator(r"^[a-z\d\-_\s]+$", 'Alphanumeric')

valid_letters_DC=RegexValidator(r"^[DdCc]+$", 'D or C')
  
class voucher_create_Form(forms.ModelForm):
  accno = forms.ModelChoiceField(
    queryset = chart_acct.objects.filter(
      chrt_H_D__in =['D','d']
    ))
  dc = forms.CharField(label='Debit or Credit',
    validators=[valid_letters_DC],
    widget=forms.TextInput(
      attrs={'class':'form-control','placeholder':'D or C'},
      )) 
    
  class Meta :
    model = voucher_creation
    fields=('accno', 'voucher_group','dc')
  def __init__(self, *args, **kwargs):
        super(voucher_create_Form, self).__init__(*args,**kwargs)
        self.fields['accno'].queryset = chart_acct.objects.filter(chrt_H_D='D')    



class DateInput(forms.DateInput):
  input_type = 'date'

class acctMasterForm(forms.Form):
  accno = forms.CharField()

class JoinForm(forms.Form):  
  email=forms.EmailField()
  name=forms.CharField(max_length=100)

class CreateAcctMasterForm(forms.ModelForm):
  chrt_accno = forms.CharField(label='Account Number',
    widget=forms.TextInput(attrs={'placeholder':'Acct No'})) 
  chrt_desc =  forms.CharField(label='Description',
                               widget=forms.TextInput(attrs={'placeholder':'Description '})) 
  chrt_H_D =  forms.CharField(label='Header',widget=forms.TextInput(attrs={'placeholder':'Header'}))  

  class Meta :
    model = chart_acct
    fields=('chrt_accno','chrt_desc','chrt_H_D','beg_bal',)
    
  def  clean_chrt_accno(self,*args,**kwargs):
    chrt_accno= self.cleaned_data.get('chrt_accno')
    if (chrt_accno==''):
      raise forms.ValidationError('Account number should be entered ')
    
    for instance in chart_acct.objects.all():
      if instance.chrt_accno == chart_acct:
        print(f'\n\n account number exists\n')
        raise forms.ValidationError('Account number already exists')

    return chrt_accno
  

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
    self.fields['chrt_accno'].disabled=True
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

class DeleteRecordMyValidator(forms.ModelForm):    
  class Meta :
    model = myvalidator
    fields=('val_user','mobile_no',)

  def __init__(self,*args,**kwargs):
    super(DeleteRecordMyValidator,self).__init__(*args,**kwargs)    
    self.fields['val_user'].disabled=True
    self.fields['mobile_no'].disabled=True      
# voucher group




class DeleteRecordVoucherGroup(forms.ModelForm):    
  class Meta :
    model = voucher_creation
    fields=('accno','author','voucher_group','dc')
  def __init__(self,*args,**kwargs):
    super(DeleteRecordVoucherGroup,self).__init__(*args,**kwargs)    
    self.fields['accno'].disabled=True
    self.fields['author'].disabled=True    
    self.fields['voucher_group'].disabled=True    
    self.fields['dc'].disabled=True    

class UpdateRecordVoucherGroup(forms.ModelForm):    
  class Meta :
    model = voucher_creation
    fields=('accno','voucher_group','author','dc',)

  def __init__(self,*args,**kwargs):
    super(UpdateRecordVoucherGroup,self).__init__(*args,**kwargs)    
    self.fields['accno'].disabled=True
    
    self.fields['voucher_group'].disabled=False    
    self.fields['author'].disabled=False    
    self.fields['dc'].disabled=False    
    
# vouchergroup test
class vouchergroup_createform(forms.ModelForm):
  accno = forms.ModelChoiceField(
    queryset = chart_acct.objects.filter(
      chrt_H_D__in =['D','d']
    )
  )
  class Meta :
    model = CreateVoucherGroup
    fields=('accno', 'desc',)


class vouchergroup_deleterecord_form(forms.ModelForm):
  
  class Meta :
    model = CreateVoucherGroup
    fields=('accno', 'desc',)
  def __init__(self,*args,**kwargs):
    super(vouchergroup_deleterecord_form,self).__init__(*args,**kwargs)    
    self.fields['accno'].disabled=True
    self.fields['desc'].disabled=True   

# my validator
class myValidatorForm(forms.ModelForm):
  class Meta :
    model = myvalidator
    fields=( 'val_user','mobile_no','name')

class UpdateRecordMyValidator(forms.ModelForm):    
  class Meta :
    model = myvalidator
    fields=('val_user','mobile_no',)

  def __init__(self,*args,**kwargs):
    super(UpdateRecordMyValidator,self).__init__(*args,**kwargs)    
    self.fields['val_user'].disabled=True
    self.fields['mobile_no'].disabled=False      

class myvalidator_Create_Form(forms.ModelForm):
  birth_date = forms.DateField(
    widget=DateInput
  )
  place_birth = forms.CharField(
    max_length=10,
    validators=[alphanumeric],

  )
  class Meta :
    model = myvalidator
    fields=('mobile_no','name', 'birth_date','place_birth')
        