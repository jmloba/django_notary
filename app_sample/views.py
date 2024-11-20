from typing import Any
from django.shortcuts import render, redirect
import datetime
from app_accounts.utils import reformat_date, date_format2
from app_notary.models import Notarized_Documents, Notary_Category
from app_accounting.models import chart_acct
from app_sample.models import StudentRec

from app_accounting.forms import CreateAcctMasterForm, UpdateRecordChrtMastForm, DeleteRecordChrtMastForm

from .forms import ChartAcctForm, ChartAcctUpdateForm,VoucherCreateForm, StudentForm

from django.views.generic import FormView, TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

# ====== class based view
class chrt_List(ListView):
  # to access the list from this model -> chrt_acct_list
  model = chart_acct  
  template_name='app_sample/chart_acct_list.html'
  # ?????
  context_object_name='chart_acct_list'
  paginate_by=4
  # queryset= chart_acct.objects.all()[:2]
  # ordering=['chrt_accno']
  def get_queryset(self):
    return chart_acct.objects.all()

class chrtmast_templateview(TemplateView) : 
  template_name = 'app_sample/chrtmast-TemplateView.html'
  model=chart_acct

  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    # templateview index
    context={
      'objects_list': self.model.objects.all().order_by('-chrt_accno'),
      'notary_category' : Notary_Category.objects.all()
    }
    return context
  
class student_templateview(TemplateView) : 
  template_name = 'app_sample/student-dashboard.html'
  model=StudentRec

  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    # templateview index
    context={
      'objects_list': self.model.objects.all().order_by('studno'),
     
    }
    return context  
  
class student_DeleteRecord(DeleteView):
  template_name='app_sample/student_DeleteView.html'
  model = StudentRec
  
  def get_success_url(self):
    return reverse_lazy('app_sample:Studentlist-View')
  
class studentCreateRec(CreateView):
  template_name='app_sample/student-CreateView.html'
  form_class = StudentForm
  
  def get_success_url(self):
    return reverse_lazy('app_sample:Studentlist-View')
  
class studentUpdateRec(UpdateView): 
  template_name='app_sample/student-UpdateView.html'
  
  form_class = StudentForm
  model = StudentRec
  def get_success_url(self):
    return reverse_lazy('app_sample:Studentlist-View')

class chrtmast_Create(CreateView) :
  model = chart_acct
  fields=['chrt_accno','chrt_desc','chrt_H_D','beg_bal']
  success_url=reverse_lazy('appSample-Dashboard')


class chrtmast_Create_Record(CreateView):
  template_name='app_sample/CreateAcctRec.html'
  form_class = ChartAcctForm
  success_url= '/template-view'

class voucherCreateView(CreateView): 
  template_name='app_sample/VoucherCreateView.html'
  form_class = VoucherCreateForm
  success_url= '/template-view'
 
class chrtmast_Update_Record(UpdateView):
  template_name='app_sample/CreateAcctRec.html'
  form_class = ChartAcctUpdateForm
  model = chart_acct
  success_url= '/template-view'

class chrtmast_Delete_Record(DeleteView):
  template_name='app_sample/chart_Delete_View.html'
  model = chart_acct
  
  def get_success_url(self):
    return ('/template-view')
  
class chartmast_Details(DetailView) : 
  template_name='app_sample/chart_Detail.html'
  model = chart_acct

class chrtmast_templateview2(TemplateView) : 
  print(f'template view')


class formview(FormView) :
  template_name = 'app_sample/chartmast_form_view.html'  
  form_class = 'CreateAcctMasterForm'
  success_url ='/'


class chrtmast_Detail(DetailView) :
  model = chart_acct
  template_name= 'chart_template.html'
  # context_object_name= 'chart_acct'
  # print(f'chrtmast detail')

class chrtmast_update(UpdateView)  :
  model = chart_acct
  fields=['chrt_accno','chrt_desc','chrt_H_D','beg_bal']
  success_url=reverse_lazy('appSample-Dashboard')

class chrtmast_Delete(DeleteView)  :  
  model = chart_acct
  context_object_name='chrtmast_rec'
  success_url=reverse_lazy('appSample-Dashboard')
# ======
def appsample_Dashboard(request):
  chrtmast = chart_acct.objects.all().order_by('chrt_accno')
  form = CreateAcctMasterForm()
  context = { 'chrtmast': chrtmast, 'form':form}  
  return render(request,'app_sample/sample-dashboard.html',context)

def appsample_deleterecord(request, pk=None):
  datarec= chart_acct.objects.get(id=pk)
  form = DeleteRecordChrtMastForm(instance =datarec) 
  if request.method=='POST':
    datarec.delete()   
    return redirect('app_sample:appSample-Dashboard', )
  context={'form':form,'datarec':datarec}
  return render(request,'app_sample/delete_chrtacct_record.html',context)

def create_master(request):
  if request.method=='POST':
    form = CreateAcctMasterForm(request.POST )
    if form.is_valid():
      print('form is valid')
      s=form.save(commit=False)
      s.val_user = request.user
      s.save()
      form=CreateAcctMasterForm()
      info = 'The record was saved successfully'
      chrtmast = chart_acct.objects.all().order_by('chrt_accno')
      context ={'form':form,'chrtmast':chrtmast}

      
      return render(request,'app_sample/sample-dashboard.html',context)
  else:  
    form =CreateAcctMasterForm()
  context={'form':form,}
  return render(request,'app_sample/create-master.html',context)

def update_chrtmast(request,pk=None):
  datarec= chart_acct.objects.get(id=pk)
  form = UpdateRecordChrtMastForm(instance =datarec)
  if request.method=='POST':

    form = UpdateRecordChrtMastForm(request.POST or None, instance = datarec)
    if form.is_valid():  
      datarec.save()
      return redirect('app_sample:appSample-Dashboard', )
  context={'form':form,'datarec':datarec}
  return render(request,'app_sample/update-chartmast-record.html',context)

def date_sample(request):
  date_today = datetime.datetime.now()
  now=datetime.datetime.now()
  print("Date: "+ now.strftime("%Y-%m-%d")) #this will print **2018-02-01** that is todays date
  '''reformat date'''

  reformated_date= reformat_date (now)
  dateformat2=date_format2(now)
  '''filter date'''

  mdata1_date = Notarized_Documents.objects.filter(created__year=2024)
  mdata1_date = Notarized_Documents.objects.filter(created__day=17)
  '''filter between dates'''
  mdata1_date=Notarized_Documents.objects.filter(created__range=["2024-07-01", "2024-07-31"])

  mdata1_date=Notarized_Documents.objects.filter(created__year='2024',                      created__month='07')


  context={'date_today':date_today ,
           'reformated_date': reformated_date,
           'dateformat2' : dateformat2,
           'mdata1_date':mdata1_date,
           }
  return render(request,'app_sample/date_sample1.html', context)

