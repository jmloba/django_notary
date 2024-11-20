from django.shortcuts import render,redirect
from django.http import JsonResponse, FileResponse,HttpResponse
from django.db import connection,IntegrityError
from app_accounting.models import chart_acct,voucher_creation, myvalidator,CreateVoucherGroup

from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from app_accounting.forms import CreateAcctMasterForm, UpdateRecordChrtMastForm, DeleteRecordChrtMastForm, DeleteRecordMyValidator, myvalidator_Create_Form, UpdateRecordMyValidator, voucher_create_Form,DeleteRecordVoucherGroup,UpdateRecordVoucherGroup 
# form for testing
from app_accounting.forms import vouchergroup_createform,vouchergroup_deleterecord_form
from django.db.models import Q
from django.urls import reverse_lazy, reverse

# dashboards
def acct_dashboard(request):
  chrtmast = chart_acct.objects.all().order_by('chrt_accno')
  form = CreateAcctMasterForm()
  context = { 'chrtmast': chrtmast, 'form':form}  
  return render(request,'app_accounting/accounting-dashboard.html',context)

def acct_dashboard_myvalidator(request):
  data = myvalidator.objects.all().order_by('mobile_no')
  context = { 'data': data}  
  return render(request,'app_accounting/accounting-myvalidator-dashboard.html',context)

def acct_dashboard_voucher_creation(request):
  data =  voucher_creation.objects.all()
  context = { 'data': data}  
  return render(request,'app_accounting/accounting-dashboard-voucher-creation.html',context)

#voucher group
def create_voucher_group(request):
  if request.method=='POST':
    form = voucher_create_Form(request.POST or None)
    if form.is_valid():
      print('form is valid')
      s=form.save(commit=False)
      s.author = request.user
      s.save()
      return redirect('app_accounting:acct-dashboard-voucher-creation' )
    else:
      print(f'form is invalid')
  else : 
    form = voucher_create_Form()

  context={'form':form,}
  return render(request,'app_accounting/create-vouchergroup-record.html',context)


def delete_vouchergroup_record(request, pk=None):
  datarec= voucher_creation.objects.get(id=pk)
  form = DeleteRecordVoucherGroup(instance =datarec) 

  if request.method=='POST':
    datarec.delete()   
    return redirect('app_accounting:acct-dashboard-voucher-creation' )
  else:
    context={'form':form,'datarec':datarec}

  return render(request,'app_accounting/delete-voucher-group-record.html',context)
def update_vouchergroup_record(request, pk=None):
  datarec= voucher_creation.objects.get(id=pk)
  form = UpdateRecordVoucherGroup(instance =datarec)
  if request.method=='POST':

    form = UpdateRecordVoucherGroup(request.POST or None, instance = datarec)
    if form.is_valid():  
      form.save()
      return redirect('app_accounting:acct-dashboard-voucher-creation', )
    else :
      print('invalid form - update vouchergroup')
      form = UpdateRecordVoucherGroup(instance =datarec)
  context={'form':form,'datarec':datarec}
  return render(request,'app_accounting/update-vouchergroup-record.html',context)

# voucher creation listview
class voucherCreation_ListView(ListView):
  template_name =('app_accounting/vouchercreation_listview.html')
  model =voucher_creation
  context_object_name='vouchergrouplist'

class voucherCreation_Create(CreateView):
  template_name='app_accounting/voucherCreationCreateView.html'
  form_class = voucher_create_Form
  def form_valid(self,form):
    form.instance.author= self.request.user
    print(f'chart accno : {self.request.POST}')
    
    return super().form_valid(form)
  def get_success_url(self):
    return reverse_lazy('app_accounting:voucher-creation-listview')  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'].fields['accno'].queryset = chart_acct.objects.filter(chrt_H_D='D')    
    
    return context

class voucherCreation_DeleteView(DeleteView):
  template_name='app_accounting/voucherCreationDeleteView.html'
  model = voucher_creation
  def get_success_url(self):
    return reverse_lazy('app_accounting:voucher-creation-listview')  
  
class voucherCreation_UpdateView(UpdateView):
  template_name='app_accounting/voucherCreationUpdateView.html'
  form_class = voucher_create_Form
  model = voucher_creation

  def form_valid(self,form):
    form.instance.author= self.request.user
    return super(voucherCreation_UpdateView,self).form_valid(form)
  
  def get_success_url(self):
    return reverse_lazy('app_accounting:voucher-creation-listview')  
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'].fields['accno'].queryset = chart_acct.objects.filter(chrt_H_D='D')    
  
    return context


# chart of account
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
      context ={'form':form,'info':info,'chrtmast':chrtmast}

      
      return render(request,'app_accounting/accounting-dashboard.html',context)
  else:  
    form =CreateAcctMasterForm()
  context={'form':form,}
  return render(request,'app_accounting/create-master.html',context)

def create_master_modal(request):

  if request.method=='POST':
    form = CreateAcctMasterForm(request.POST )
    chrtmast = chart_acct.objects.all().order_by('chrt_accno')    
    if form.is_valid():
      form = CreateAcctMasterForm(request.POST )
      
      print('form is valid')
      s=form.save(commit=False)
      s.val_user = request.user
      s.save()
      info = f'Account {s.chrt_accno} has been created succesfully'
      context = { 'chrtmast': chrtmast, 'form':form,'info':info}  
      return render(request,'app_accounting/accounting-dashboard.html',context)
    else:
      print('form is invalid ')
      context = { 'chrtmast': chrtmast, 'form':form,}  
      return render(request,'app_accounting/accounting-dashboard.html',context)
    
      
  else:
    print('methos is not post')
    form =CreateAcctMasterForm()
    chrtmast = chart_acct.objects.all().order_by('chrt_accno')
    context ={'form':form,'chrtmast':chrtmast}
    return render(request,'app_accounting/accounting-dashboard.html',context)
  
def create_master_ajax(request):
  form =CreateAcctMasterForm()
  context={'form':form,}
  return render(request,'app_accounting/create-master-ajax.html',context)

def submitCreateNewRecord(request):

  if request.method == 'POST':
    accno = request.POST['accno']
    desc = request.POST['desc']
    header = request.POST['header']
    bbal = request.POST['bbal']

    form = CreateAcctMasterForm(request.POST )

    print(f'fields are : \n accno :{accno} \n desc : {desc}\n header :{header}\n bbal : {bbal}')
    
    if form.is_valid():
      form.save()
      accno = request.POST.get()
      accnois = f'accno : is : {accno}'
      print(f'in ajax {accno}')

      datalist={'status':'status is ok','accnois':accnois}
      return JsonResponse(datalist)
    else :  
      return JsonResponse({'status':form.errors,})
  else :
    return JsonResponse({'status':'not post',})



def update_record(request, pk=None):
  datarec= chart_acct.objects.get(id=pk)
  form = UpdateRecordChrtMastForm(instance =datarec)
  if request.method=='POST':

    form = UpdateRecordChrtMastForm(request.POST or None, instance = datarec)
    if form.is_valid():  
      datarec.save()
      return redirect('app_accounting:acct-dashboard', )
  context={'form':form,'datarec':datarec}
  return render(request,'app_accounting/update-chartmast-record.html',context)
def delete_record(request, pk=None):
  datarec= chart_acct.objects.get(id=pk)
  form = DeleteRecordChrtMastForm(instance =datarec) 
  if request.method=='POST':
    datarec.delete()   
    return redirect('app_accounting:acct-dashboard', )
  context={'form':form,'datarec':datarec}
  return render(request,'app_accounting/delete-record.html',context)

# myvalidator
def myvalidator_create_record(request):
  if request.method=='POST':
    form = myvalidator_Create_Form(request.POST )
    if form.is_valid():
      print('form is valid')
      s=form.save(commit=False)
      s.val_user = request.user
      s.save()
      return redirect('app_accounting:acct-dashboard-myvalidator' )
  else:  
    form =myvalidator_Create_Form()
  context={'form':form,}
    
  return render(request,'app_accounting/create-myvalidator-record.html',context)
def myvalidator_delete_record(request, pk=None):
  datarec= myvalidator.objects.get(id=pk)
  form = DeleteRecordMyValidator(instance =datarec) 
  if request.method=='POST':
    datarec.delete()   
    return redirect('app_accounting:acct-dashboard-myvalidator' )
  context={'form':form,'datarec':datarec}
  return render(request,'app_accounting/delete-record-myvalidator.html',context)
def myvalidator_update_record(request, pk=None):
  datarec= myvalidator.objects.get(id=pk)
  form = UpdateRecordMyValidator(instance =datarec)

  if request.method=='POST':

    form = UpdateRecordMyValidator(request.POST or None, instance = datarec)
    if form.is_valid():  
      datarec.save()
      return redirect('app_accounting:acct-dashboard-myvalidator', )

  context={'form':form,'datarec':datarec}
  return render(request,'app_accounting/update-myvalidator-record.html',context)
#orm test
def orm_dashboard(request):
  data = CreateVoucherGroup.objects.all().order_by('accno') 
  print(f'\ndata: -->>> {data}\n')
  
  data_query = data.query
  print(f'\ndata: -->>> {data.query}\n')

  
  data_filter = CreateVoucherGroup.objects.filter(desc__startswith='desc')

  # using union 
  data_union = CreateVoucherGroup.objects.all().values_list('accno','desc')
  # .union(chart_acct.objects.all().values_list('chrt_accno','chrt_desc'))

  union_con_queries = connection.queries

  data_union_query = data_union.query
  context = { 
    'data': data,
    "data_query":data_query, 
    "data_filter": data_filter.query,

    
    'data_union':data_union,
    'data_union_query': data_union_query,
    'union_con_queries':union_con_queries
    

    }  
 
  return render(request,'app_accounting/orm-dashboard.html',context)  
def vouchergroup_test_createrecord(request):
  if request.method=='POST':
    form =vouchergroup_createform(request.POST)
    if form.is_valid():
          form.save()
          return redirect('app_accounting:orm-dashboard' )    


  else:  
    form =vouchergroup_createform()
  context={'form':form,}
  return render(request,'app_accounting/vouchergroup-test-add.html',context)
def vouchergroup_test_deleterecord(request,pk:None):
  datarec= CreateVoucherGroup.objects.get(id=pk)

  form = vouchergroup_deleterecord_form(instance =datarec) 

  if request.method=='POST':
    datarec.delete()   
    return redirect('app_accounting:orm-dashboard' )   
  else:
    context={'form':form,'datarec':datarec}
    
  return render(request,'app_accounting/delete-orm-vouchergroup.html',context)

# orm query-set
def update_queryset(request):
  vouchergroup_rec = CreateVoucherGroup.objects.first()
  vouchergroup_rec.desc = "first record"
  vouchergroup_rec.save(update_fields=['desc'])

  return redirect('app_accounting:orm-dashboard' )   

def queryset_filter_startwith(request):
  print(f'\nstartswith:::\n') 
  orm = f" CreateVoucherGroup.objects.filter(desc__startswith='f') "
  data = CreateVoucherGroup.objects.filter(desc__startswith='f')
                                           
  print(f'\ndata: -->>> {data}\n')
  print(f'\ndata: -->>> {data.query}\n')
  data_query = data.query

  data_filter = CreateVoucherGroup.objects.filter(desc__startswith='first')
  context = { 
    'orm':orm,
    'data': data,
    "data_query":data_query, 
    "data_filter": data_filter.query

    }  

  return render(request,'app_accounting/orm-dashboard.html',context)  
def queryset_usingQ(request):
  print(f'\query set using Q:::\n') 
  orm = f" CreateVoucherGroup.objects.filter(Q(desc__startswith='f') |  Q(desc__startswith='s')) "
  data = CreateVoucherGroup.objects.filter(
    Q(desc__startswith='f') |  Q(desc__startswith='s')
                                           )
                                           
  print(f'\ndata: -->>> {data}\n')
  print(f'\ndata: -->>> {data.query}\n')
  data_query = data.query
  data_connection  = connection.queries

  data_filter = CreateVoucherGroup.objects.filter(
    Q(desc__startswith='f') &  Q(desc__startswith='s')
                                           )
  context = { 
    'orm':orm,
    'data': data,
    "data_query":data_query, 
    "data_filter": data_filter.query,
    "data_connection" : data_connection

    }  

  return render(request,'app_accounting/orm-dashboard.html',context)  

# triggers from javascript
# passing parameter from url
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def get_accname(request):

  if request.method == 'POST':
    print('method is  post')
    if is_ajax(request):
      accno = request.POST['accno']
      data = list(chart_acct.objects.filter(chrt_accno=accno).values_list('chrt_desc'))


      print(f'\ndata queryset list {data}\n')



      response = {'status':'Success', 'data': data}
      return JsonResponse( response )
    else : 
      print('not ajax')
  
  else:  
    print('method is not post')
    
   
    response = {'status':'failed', 'Message': 'request is not post !!!'}
    return JsonResponse(response)   
  
def sample_popup_return_value  (request):
  data = chart_acct.objects.all()

# sample 



 