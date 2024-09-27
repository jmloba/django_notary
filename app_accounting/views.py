from django.shortcuts import render,redirect
from app_accounting.models import chart_acct
from app_accounting.forms import CreateAcctMasterForm, UpdateRecordChrtMastForm,DeleteRecordChrtMastForm

# Create your views here.

def acct_dashboard(request):
  chrtmast = chart_acct.objects.all().order_by('chrt_accno')

  context = { 'chrtmast': chrtmast}  
  # return render(request,'app_accounting/acct-master.html',context)

  return render(request,'app_accounting/accounting-dashboard.html',context)


def create_master(request):
  form =CreateAcctMasterForm()
  context = {'form':form }
  if request.method=='POST':
    form = CreateAcctMasterForm(request.POST or None )
    if form.is_valid():
      print('form is valid')
      s=form.save(commit=False)
      s.chrt_user = request.user

      s.save()

      chrtmast = chart_acct.objects.all().order_by('chrt_accno')

      context = { 'chrtmast': chrtmast}  
      return redirect('app_accounting:acct-dashboard' )

    else:  
      print(f'Creating Record  error: {form.errors}' )
      return redirect('app_accounting:acct-dashboard' )

    
  return render(request,'app_accounting/create-master.html',context)

def delete_record(request, pk=None):
  datarec= chart_acct.objects.get(id=pk)
  form = DeleteRecordChrtMastForm(instance =datarec) 

  if request.method=='POST':
    datarec.delete()   
    return redirect('app_accounting:acct-dashboard', )

  context={'form':form,'datarec':datarec}
  return render(request,'app_accounting/delete-record.html',context)

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