from django.shortcuts import render
from django.http import HttpResponse
from django_htmx.http import HttpResponseClientRedirect,HttpResponseClientRefresh,HttpResponseLocation

from app_notary.models import Notary_Category,Notarized_Documents

# Create your views here.
def app_htmx_main(request):
  print(request.htmx)  
  print(request.htmx.target)
  print(request.htmx.trigger)
  print(request.htmx.boosted)
  data=Notarized_Documents.objects.all()
  if request.htmx:
     print('request is htmx')
  else:    
     print('request is not htmx')

  context={'data':data}
  return render(request,'app_htmx/app-htmx-main.html',context)  
  
def open_admin(request):
  data=Notarized_Documents.objects.all()
  if request.htmx:
    print(f' it is now htmx request')
    print(f'boosted : {request.htmx.boosted}')
    mlorem='lorem'
    context={'mlorem':mlorem}  
    # return render(request,'app_htmx/lorem.html',context)  
    return HttpResponseClientRedirect('/admin/')
    # return HttpResponseClientRefresh()
  else:
    context={'data':data}
    return render(request,'app_htmx/app-htmx-main.html',   context)      

def app_test(request):
    context={}  
    return render(request,'app_htmx/test.html',context)  

def app_htmx_button1_refresh(request):
  data=Notarized_Documents.objects.all()
  if request.htmx:
    print(f' it is now htmx request')
    print(f'boosted : {request.htmx.boosted}')
    mlorem='lorem'
    context={'mlorem':mlorem}  
    # return render(request,'app_htmx/lorem.html',context)  
    # return HttpResponseClientRedirect('/admin/')
    return HttpResponseClientRefresh()
  else:
    context={'data':data}
    return render(request,'app_htmx/app-htmx-main.html',   context)   
def display_lorem(request):
  data=Notarized_Documents.objects.all()
  if request.htmx:
    print(f'display lorem : a it is now htmx request')
    print(f'boosted : {request.htmx.boosted}')

    mlorem='lorem'
    context={'mlorem':mlorem}  
    return render(request,'app_htmx/lorem.html',context)  
  else:
    context={'data':data}
    return render(request,'app_htmx/app-htmx-main.html',   context)   
  

  
  
def open_admin(request):
  data=Notarized_Documents.objects.all()
  if request.htmx:
    print(f' it is now htmx request')
    print(f'boosted : {request.htmx.boosted}')

    mlorem='lorem'
    context={'mlorem':mlorem}  
    # return render(request,'app_htmx/lorem.html',context)  
    return HttpResponseClientRedirect('/admin/')
    # return HttpResponseClientRefresh()
    
  
  else:
    context={'data':data}
    return render(request,'app_htmx/app-htmx-main.html',   context)      


def success(request):
    return HttpResponse('Congratulations')

def app_htmx_success(request):
  print('views success')
  if request.htmx:
    return HttpResponse('Congratulations')
  else :
    data=Notarized_Documents.objects.all()    
    context={'data':data}
    return render(request,'app_htmx/app-htmx-main.html',   context)    

def button_4(request) :
  data=Notarized_Documents.objects.all()
  if request.htmx:     
    print(f'button_4 : a it is now htmx request / httpresponse location')
    print(f'boosted : {request.htmx.boosted}')
    return HttpResponseLocation("/success/")
