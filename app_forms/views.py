from django.shortcuts import render,redirect
from app_notary.models import Notarized_Documents, Notary_Category
from app_forms.forms import CreateRecordNotaryForm,UpdateRecordNotaryForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='app_accounts:login_view')
def notary_list(request):
  
  data=Notarized_Documents.objects.all()
  form = CreateRecordNotaryForm()

  context={'data':data, 'form':form}
  return render(request,'app_forms/sample1.html',context)  

@login_required(login_url='app_accounts:login_view')
def create_notary(request):
  form = CreateRecordNotaryForm()
  if request.method == 'POST' :
    print(f'request.form is post : -->> {request.POST}')
    data=Notarized_Documents.objects.all()
    form = CreateRecordNotaryForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
      print(f'form is valid')

      s=form.save(commit = False)
      s.user=request.user
      s.save()
    else: 
      print(f'form is not valid {form.errors}')
  context = {'form':form, 'data': data}  
  return render(request,'app_forms/sample1.html',context)

@login_required(login_url='app_accounts:login-view')
def dashboard(request):
  data=Notarized_Documents.objects.all()
  form = CreateRecordNotaryForm()

  context={'data':data, }
  return render(request,'app_forms/dashboard.html',context)

@login_required(login_url='app_accounts:login-view')
def create_record(request):
  form = CreateRecordNotaryForm()
  if request.method=='POST':
    form = CreateRecordNotaryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
      s=form.save(commit=False)
      s.user = request.user 
      s.save()
      data=Notarized_Documents.objects.all()
      context={'data':data, }

      return redirect('app_forms:dashboard', )
    else:
      return redirect('app_forms:dashboard' )
      print(f'create_record form is not valid ')
  context={'form':form, }
  return render(request,'app_forms/create-record.html',context)


@login_required(login_url='app_accounts:login-view')


def update_record(request, pk=None):

  datarec= Notarized_Documents.objects.get(id=pk)

  form = UpdateRecordNotaryForm(instance =datarec)

  if request.method=='POST':

    form = UpdateRecordNotaryForm(request.POST or None, request.FILES or None, instance = datarec)
    if form.is_valid():  
      form.save()
      return redirect('app_forms:dashboard', )

  context={'form':form,'datarec':datarec}
  return render(request,'app_forms/update-record.html',context)

def delete_record(request, pk=None):
  
  datarec= Notarized_Documents.objects.get(id=pk)
  form = UpdateRecordNotaryForm(instance =datarec)   

  if request.method=='POST':

    datarec.delete()   
    return redirect('app_forms:dashboard', )


  context={'form':form,'datarec':datarec}
  return render(request,'app_forms/delete-record.html',context)