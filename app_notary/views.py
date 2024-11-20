from django.shortcuts import get_object_or_404, render

from .models import Notary_Category, Notarized_Documents
from django.http import JsonResponse, FileResponse,HttpResponse

from .forms import Notary_form, Notary_Categoryform, Notary_form_A
from django.template.loader import render_to_string

# Create your views here.




def data_list():

  mrec=Notary_Category.objects.all().values('doc_category',)
  mlist = list(mrec)
  return mlist

def notary_input(request):
  form = Notary_form()
  data = Notarized_Documents.objects.all()

  context={ 'form': form, 'data':data}
  return render(request,'app_notary/notary-input.html', context)

def category_entry(request):
  form = Notary_Categoryform()
  data = Notary_Category.objects.all()

  context={ 'form': form, 'data':data}

  return render(request,'app_notary/category-main.html', context)


def notary_entry(request):
  form = Notary_form_A(request.POST or None , request.FILES or None)
  data=Notarized_Documents.objects.all()

  context={ 'form': form, 'data':data}
  return render(request,'app_notary/notary-entry.html', context)

def notary_edit(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    rec = Notarized_Documents.objects.get(pk=id)
    category_desc=rec.category.doc_category


    
    print(f'notary edit : {category_desc}')

    

    categ_data = {'status':'Success',
                  'id':rec.id, 
                  'firstname': rec.firstname, 
                  'lastname':rec.lastname,
                  'bookno': rec.bookno,
                  'pageno': rec.pageno,
                  'recordno':rec.recordno,
                  'category_desc':category_desc,
      
                  }
    
    return JsonResponse(categ_data)
  else:
    categ_data = {'status':'Failed'}
    return JsonResponse(categ_data)

def data_list():

  mrec=Notarized_Documents.objects.all().values('id','category__doc_category','firstname','lastname','created','bookno','pageno','recordno','amount', 'myimage','myfile')
  mlist = list(mrec)
  print(f'\n\ndata_list --->>:{mlist}\n')

  return mlist

def save_notary_entry(request):
   
  if request.method == 'POST':
    form = Notary_form(request.POST or None, request.FILES or None)
    if form.is_valid():
      print(f'form is valid***')
      sid =  request.POST.get('stuid')

      
      if sid=='' or sid==None:
        print('sid empty')
        doc = Notarized_Documents(user=request.user, 
              firstname   = request.POST.get('firstname'), 
              lastname    = request.POST.get('lastname'), 
              category    = Notary_Category.objects.get(id=request.POST.get('category')),
              bookno      = request.POST.get('bookno'), 
              pageno      = request.POST.get('pageno'), 
              recordno    = request.POST.get('recordno'), 
              amount = request.POST.get('amount'), 

              myimage=request.FILES.get('myimage'),
              myfile=request.FILES.get('myfile'),
              )
      else: 
        print('sid not empty')
        doc = Notarized_Documents(id=sid, 
              user=request.user, 
              firstname=request.POST.get('firstname'), 
              lastname=request.POST.get('lastname'), 
              category=Notary_Category.objects.get(id=request.POST.get('category')),
              bookno=request.POST.get('bookno'), 
              pageno=request.POST.get('pageno'), 
              recordno=request.POST.get('recordno'), 
              amount = request.POST.get('amount'), 

              myimage=request.FILES.get('myimage'),
              myfile=request.FILES.get('myfile'),              
              )
        
      doc.save()  


      firstname= doc.firstname
      lastname = doc.lastname


      print(f'data has been saved')
      datalist=data_list()
      return JsonResponse({'status':'Success','datalist':datalist,'firstname': firstname,'lastname':lastname})

    else :
      return JsonResponse({'status':'Invalid Form',})
    

def save_notary_input(request):
  if request.method == 'POST':
    form = Notary_form(request.POST or None)
    if form.is_valid():
      print(f'form is valid***')
      sid =  request.POST.get('stuid')

      if sid=='':
        print('sid empty')
        doc = Notarized_Documents(user=request.user, 
              firstname=request.POST.get('firstname'), 
              lastname=request.POST.get('lastname'), 
              category=Notary_Category.objects.get(id=request.POST.get('category'))

              )
      else: 
        print('sid not empty')
        doc = Notarized_Documents(id=sid, 
              user=request.user, 
              firstname=request.POST.get('firstname'), 
              lastname=request.POST.get('lastname'), 
              category=Notary_Category.objects.get(id=request.POST.get('category'))

              )
        
      doc.save()  

      firstname= doc.firstname
      lastname = doc.lastname
      print(f'data has been saved')
      datalist=data_list()
      response = {'status':'Success','datalist':datalist,'firstname': firstname,'lastname':lastname}
     
      return JsonResponse(response)

    else :
      return JsonResponse({'status':'Invalid Form',})
    
def notary_delete(request):
  if request.method == "POST":  
    print(f'notary delete post ok')
    id = request.POST.get("sid")
    mrec = Notarized_Documents.objects.get(pk=id)
    
    mrec.delete()

    notary_data =   Notarized_Documents.objects.all().values('id','category__doc_category','firstname','lastname','created', )
    data=list(notary_data)
          
    invoice_total_qty=0
    invoice_amount=0
    return JsonResponse({"status": 1, "data":data,'message':'data deleted'
                         })
  else:
    return JsonResponse({"status": 0})  
  
def notary_delete_cairo_coder(request):

  if request.method == "POST":  
    print(f'notary delete post ok')
    return JsonResponse({"status": 1, })
  else:
    return JsonResponse({"status": 0})      
  
def notary_entry_modal(request):

  notary_list=Notarized_Documents.objects.all()

  context={  'notary_list':notary_list}
  return render(request,'app_notary/notary-entry-modal.html', context)

def save_notary_form(request, form ,template_name):
  print('---> save notary form ')
  # initialize data as dictionary
  data= dict()
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      data['form_is_valid'] = True
      notary_list = Notarized_Documents.objects.all()

      data['html_notary_list']= render_to_string('app_notary/partial_notary_list.html',{'notary_list':notary_list})
    else:
      data['form_is_valid'] = False

  context ={'form':form}
  data['html_form'] = render_to_string(template_name, context, request=request)
  return JsonResponse(data)

def modal_notary_create(request):
  if request.method=='POST':
    form = Notary_form(request.POST or None, request.FILES or None )
  else:
    print('request is not post')
    form = Notary_form()

  return save_notary_form(request, form,'app_notary/partial_notary_create.html')  


def modal_notary_update(request,pk=None):
  product=get_object_or_404(Notarized_Documents,pk=pk)
  if request.method =='POST':
    form=Notary_form(request.POST, instance=product)
  else:
    form=Notary_form( instance=product)
  return save_notary_form(request, form,'app_notary/partial_notary_update.html')  



def modal_notary_delete(request,pk=None):  
  
  notary_item =get_object_or_404(Notarized_Documents,pk=pk)
  data = dict()

  if request.method =='POST':
    notary_item.delete()

    data['form_is_valid'] = True
    notary_list = Notarized_Documents.objects.all()
    context = {'notary_list':notary_list}

    data['html_notary_list']= render_to_string('app_notary/partial_notary_list.html',context)

  else:
    context={'notary_item':notary_item}
    data['html_form'] = render_to_string('app_notary/partial_notary_delete.html',context, request=request)
    
  return JsonResponse(data)


    