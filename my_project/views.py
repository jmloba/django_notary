
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse

def home(request):
  # customers=Customer.objects.all()
  context = {
    
  }
  return render(request,'home.html',context )