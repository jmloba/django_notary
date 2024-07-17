from django import forms 

from app_notary.models import Notarized_Documents, Notary_Category

class CreateRecordNotaryForm(forms.ModelForm):
  class Meta :
    model= Notarized_Documents
    fields=('category','firstname','lastname','myfile','myimage','address','bookno','pageno', 'recordno','amount_paid')

    labels={
      'category':'Category',
      'firstname':'First Name',
      'lastname':'Last Name',
      'address':'Address',

      'myimage': 'Image',
      'myfile':'Attached document',
      'bookno' :'Book No.',
      'pageno':'Page No.',
      'recordno':'Record No.',
      'amount_paid': 'Amount Paid',

    }
  def __init__(self,*args,**kwargs):
    super(CreateRecordNotaryForm,self).__init__(*args,**kwargs)
    self.fields['firstname'].required=True
    self.fields['lastname'].required=True
    self.fields['category'].required=True

class UpdateRecordNotaryForm(forms.ModelForm):
  class Meta :
    model= Notarized_Documents
    fields=('category','firstname','lastname','myfile','myimage','address','bookno','pageno', 'recordno','amount_paid')

    labels={
      'category':'Category',
      'firstname':'First Name',
      'lastname':'Last Name',
      'address':'Address',
      'myimage': 'Image',
      'myfile':'Attached document',
      'bookno' :'Book No.',
      'pageno':'Page No.',
      'recordno':'Record No.',
      'amount_paid': 'Amount Paid',
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecordNotaryForm,self).__init__(*args,**kwargs)
    self.fields['firstname'].required=True
    self.fields['lastname'].required=True
    self.fields['category'].required=True    


''' Category'''    

class CreateRecordCategoryForm(forms.ModelForm):
  class Meta :
    model=Notary_Category
    fields=('doc_category',)

    labels={
      'doc_category':'Category',
    }
  def __init__(self,*args,**kwargs):
    super(CreateRecordCategoryForm,self).__init__(*args,**kwargs)
    self.fields['doc_category'].required=True
class UpdateRecordCategoryForm(forms.ModelForm):
  class Meta :
    model=Notary_Category
    fields=('doc_category',)

    labels={
      'doc_category':'Category',
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecordCategoryForm,self).__init__(*args,**kwargs)
    self.fields['doc_category'].required=True