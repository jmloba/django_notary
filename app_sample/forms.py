from django import forms
from app_accounting.models import chart_acct,voucher_creation
from app_sample.models import StudentRec 


class ChartAcctForm(forms.ModelForm):
  class Meta :
    model = chart_acct
    fields=('chrt_accno','chrt_desc','chrt_H_D','beg_bal',)
    labels = {'chrt_accno':'Account Number xx from form', 'chrt_desc':'Description', 'chrt_H_D': 'Header','beg_bal':'Begininng Balance'}
    widgets = {
      'chrt_accno': forms.TextInput(attrs={'classes':'form-control'}), 
    
    }
    def clean(self):
      fields = self.cleaned_data

class VoucherCreateForm(forms.ModelForm):
  class Meta :
    model = voucher_creation
    fields=('accno','author','voucher_group','dc',)
    labels={'accno':'Account Number', 'author':'Author','voucher_group':'Voucher Group','dc':'Header'}
    
class ChartAcctUpdateForm(forms.ModelForm):
  class Meta :
    model = chart_acct
    fields=('chrt_accno','chrt_desc','chrt_H_D','beg_bal',)
    labels = {'chrt_accno':'Account Number xx from form', 'chrt_desc':'Description', 'chrt_H_D': 'Header','beg_bal':'Begininng Balance'}
    widgets = {
      'chrt_accno': forms.TextInput(attrs={'classes':'form-control'}), 
    
    }
  def __init__(self, *args, **kwargs):
    super(ChartAcctUpdateForm, self).__init__(*args, **kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.id:
      self.fields['chrt_accno'].widget.attrs['readonly'] = True    
  def clean(self):
    fields = self.cleaned_data  

  class CreateVoucherTemplateForm(forms.ModelForm):
    accno = forms.ModelChoiceField(
      queryset = chart_acct.objects.filter(
        chrt_H_D__in =['D','d']
      )
    )

    class Meta :
      model = voucher_creation
      fields=('accno', 'voucher_group','dc')    

class StudentForm(forms.ModelForm):
  birthdate=forms.DateField(widget=forms.DateInput(
    attrs={'type':'date'})
    )  
  notes=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Description and notes', 'rows':3, 'cols':5}))
  
  class Meta :
      model = StudentRec
      fields=('studno', 'firstname','lastname','birthdate','mobile','notes')    
  
        