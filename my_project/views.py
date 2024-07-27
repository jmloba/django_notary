
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse

@login_required(login_url='app_accounts:login-view')

def home(request):
  # customers=Customer.objects.all()
  context = {
    
  }
  return render(request,'home.html',context )