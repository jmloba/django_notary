from django.shortcuts import render
import datetime
from app_accounts.utils import reformat_date, date_format2
from app_notary.models import Notarized_Documents

# Create your views here.
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
