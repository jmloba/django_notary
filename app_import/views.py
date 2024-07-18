
from django.shortcuts import render,redirect
from app_import.models import Phil_City,Phil_Province_Towns
from tablib import Dataset
from datetime import datetime

from .resources import  CityResource

# Create your views here.
def import_excel_city(request):
  print('import excel.....')
  if request.method =='POST':
    city_resource = CityResource()
    dataset = Dataset()
    new_cities = request.FILES['myfile']
    imported_data = dataset.load(new_cities.read(),format='xlsx')
    for data in imported_data:
      value= Phil_City(
        country=data[0],
        city = data[1],
        province = data[2],
        is_active = data[3],
        # created_at=datetime.now()
        # modified_at =datetime.now()

      )
      value.save()  
      


  philcity=Phil_City.objects.all()
  context= {'data':philcity}
  
  return render(request,'app_import/excel-import.html', context)


def import_province_town(request):
  if request.method =='POST':
    city_resource = CityResource()
    dataset = Dataset()
    new_cities = request.FILES['myfile']
    imported_data = dataset.load(new_cities.read(),format='xlsx')
    for data in imported_data:
      value= Phil_Province_Towns(
        towns=data[0],
        barangay_no = data[1],
        municipal_class =  data[2],
        province = data[3],
        is_active = True,
        country =  data[4],
        # created_at=datetime.now()
        # modified_at =datetime.now()

      )
      value.save()  
      


  toupdate=Phil_Province_Towns.objects.all()
  context= {'data':toupdate}
  return render(request,'app_import/excel-import-towns.html', context)

def province_town_delete(request):
  data = Phil_Province_Towns.objects.all().delete()
  return redirect('app_import:import-province-town' )

def city_delete(request):
  data = Phil_City.objects.all().delete()
  return redirect('app_import:import-excel-city')
  

def import_city_now(request):
  print(f'import city now')
 
