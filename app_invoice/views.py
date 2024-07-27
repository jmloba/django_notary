
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import JsonResponse, FileResponse,HttpResponse

from django.db.models import Sum, Q

from app_invoice.forms import InvoiceForm, Invoice, InvoiceSearchForm ,PrintInvoiceForm, DeleteRecord_CategoryForm, UpdateRecord_CategoryForm, DeleteRecord_MasterFileForm, UpdateRecord_MasterFileForm, DeleteRecord_SalesEntryForm




from .forms import Masterfile_form

from .models import Customer, Invoice, InvoiceSummary, Category_Sales,MasterFile,Ref_Table

from app_accounts.utils import date_format2, reformat_date
from app_print.views import print_invoice
from django.contrib import messages

# printing
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, letter


# Create your views here.


def data_list(request,invno)  :
  invoicedata =   Invoice.objects.filter(user=request.user, invoice_no = invno).values('id','customer','customer__name','itemnumber','invoice_no','description','invoice_date','quantity', 'price', 'amount')
  invoice_total_qty=0
  invoice_amount=0

  for i in  invoicedata:
    invoice_total_qty += i['quantity']
    invoice_amount += i['price'] *i['quantity']
    
  invoice_data= list(invoicedata)
  for i in invoice_data:
    i['invoice_date'] = reformat_date(i['invoice_date'] )
  print(f'***invoicedata  ****: {invoice_data}')  
  return invoice_data,invoice_total_qty,invoice_amount

def invoice_create(request):
  title ="Invoice Section"
  card_title='Invoice Entry'

  invoice_form =InvoiceForm()
  search_form = InvoiceSearchForm()
  mdata = Invoice.objects.filter(user=request.user, invoice_no = 0 ).values('id','customer','customer__name','itemnumber','description','invoice_date','quantity','price','amount')
  invoice_db= list(mdata)  
  for i in invoice_db:
    i['invoice_date'] = reformat_date(i['invoice_date'] )
  print(f'invoice_db-->> : {invoice_db}')
  
  if request.method=='POST':
    print('request is post....')
    search_form = InvoiceSearchForm(request.POST or None)
    invoice_db=Invoice.objects.filter(user=request.user ,description__icontains=search_form['description'].value( ))     
  else:
    print('request is GET')


  context={'title':title,
           "card_title": card_title,
           "invoice_form": invoice_form, 
           "search_form":search_form,
           "invoice_db":invoice_db          
           }
  
  
  return render(request,'app_invoice/create_invoice.html', context)
def save_invoice(request):  
  if request.method == 'POST':
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
      print(f'form is valid***')
      sid =  request.POST.get('stuid')
      amount = int( request.POST.get('quantity')) * int(request.POST.get('price'))
      if sid=='':
        s=Invoice(user=request.user,
          itemnumber =     request.POST.get('itemnumber'),    
          customer=Customer.objects.get( id=request.POST.get('customer')),
          description= request.POST.get('description'),
          quantity = request.POST.get('quantity'),
          price = request.POST.get('price'),
          amount=amount
          
          )
      else:  
        s=Invoice(id=sid,
          user=request.user, 
          itemnumber =  request.POST.get('itemnumber'),    
          customer=Customer.objects.get(id=request.POST.get('customer')),
          description= request.POST.get('description') , 
          quantity = request.POST.get('quantity'),
          price = request.POST.get('price'),
          amount=amount
          )
      
      s.save()
      invno=0
      invoice_data,invoice_total_qty,invoice_amount =data_list(request,invno)

      return JsonResponse({
        'status':'Success',
        'invoice_data':invoice_data,
        'invoice_total_qty':invoice_total_qty, 
        'invoice_amount':invoice_amount})
    
    else:
      return JsonResponse({'status':'Invalid Form',})
    
def save_invoice2(request):
  if request.method == 'POST':
    form = InvoiceForm2(request.POST or None)
    if form.is_valid():
      print(f'form is valid***')
      sid =  request.POST.get('stuid')
      amount = int( request.POST.get('quantity')) * float(request.POST.get('price'))
      if sid=='':
        s=Invoice(user=request.user,
          itemnumber =     request.POST.get('itemnumber'),    
          
          description= request.POST.get('description'),
          quantity = request.POST.get('quantity'),
          price = request.POST.get('price'),
          amount=amount
          
          )
      else:  
        s=Invoice(id=sid,
          user=request.user, 
          itemnumber =  request.POST.get('itemnumber'),    
          
          description= request.POST.get('description') , 
          quantity = request.POST.get('quantity'),
          price = request.POST.get('price'),
          amount=amount
          )
      
      s.save()
      invno=0
      invoice_data,invoice_total_qty,invoice_amount =data_list(request,invno)

      return JsonResponse({
        'status':'Success',
        'invoice_data':invoice_data,
        'invoice_total_qty':invoice_total_qty, 
        'invoice_amount':invoice_amount})

    else  :
      return JsonResponse({'status':'Invalid Form',})
def put_invoice(request,new_invoice):
  ''' 
  update the invoice number if user  and invoice value is 0
  '''
  Invoice.objects.filter(user=request.user,invoice_no = 0).update(invoice_no=new_invoice)

  qs_sum =Invoice.objects.filter(user=request.user, invoice_no = new_invoice).aggregate(Sum('quantity') , Sum('amount') ) 

  # print(f"getting the summ of total invoice :\n{qs_sum} \n sum quantity: {qs_sum['quantity__sum'] } \n sum amount : {qs_sum['amount__sum']}")


  InvoiceSummary.objects.create(user=request.user,invoice_no =new_invoice , total_quantity = qs_sum['quantity__sum'] ,total_amount=qs_sum['amount__sum'])

def get_invoice_x():
  qs =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')
  prev_val = qs[0]['ref_no']
  print(f'prev_val  :   {type(prev_val)} , {prev_val}'  )
  Ref_Table.objects.filter(reference='Sales Invoice').update(ref_no=prev_val+1)
  newval =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')
  print(f' prev_val{prev_val}, newval: {newval}')
  return prev_val
def get_invoice():
  '''get the value of  invoice  in reference table'''
  prev_val =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')[0]['ref_no']
  print(f"prev_val : {type(prev_val)} ")

  '''increment the value for the next invoice '''
  Ref_Table.objects.filter(reference='Sales Invoice').update(ref_no=prev_val+1)

  newval =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')[0]['ref_no']

  print(f"newval : {type(newval)} , {newval}")
  return newval

def print_invoicexx(request):
  form=PrintInvoiceForm()
  context={'form':form}
  return render(request,'app_invoice/print_invoice.html', context) 
def create_an_invoice(request):
  '''get the invoice no from the reference file '''
  new_invoice = get_invoice()

  put_invoice(request,new_invoice)  # resave

  # joven from appsample

  print_invoice(request,new_invoice)

  invno = 0
  invoice_data, invoice_total_qty, invoice_amount = data_list(request,invno)

  categ_data = {'status':'Success','invoice_data':invoice_data,'invoice_total_qty':invoice_total_qty,'invoice_amount':invoice_amount}

  return  JsonResponse(categ_data)
def invoice_edit(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    invoice = Invoice.objects.get(pk=id)

    categ_data = {'status':'Success',
                  'id':invoice.id, 
                  'description': invoice.description,'customer_name':invoice.customer.name
                  }
    
    print(f'*** edit {invoice.customer.name}' )
    return JsonResponse(categ_data)
  else:
    categ_data = {'status':'Failed'}
    return JsonResponse(categ_data)
def invoice_edit2(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    invoice = Invoice.objects.get(pk=id)

    categ_data = {'status':'Success',
                  'id':invoice.id, 
                  'description': invoice.description, 'itemnumber':invoice.itemnumber,
                  'quantity':invoice.quantity,
                  'price':invoice.price }

    # print(f'*** edit {invoice.customer.name}' )
    return JsonResponse(categ_data)
  else:
    categ_data = {'status':'Failed'}
    return JsonResponse(categ_data)  
def invoice_delete(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    invoice = Invoice.objects.get(pk=id)
    print(f'record to delete : {invoice}')
    invoice.delete()

    invoicedata =   Invoice.objects.filter(user=request.user, invoice_no = 0).values('id','customer','customer__name','description','invoice_date','quantity', 'price', 'amount')
          
    invoice_total_qty=0
    invoice_amount=0

    for i in  invoicedata:
      invoice_total_qty += i['quantity']
      invoice_amount += i['price'] *i['quantity']

    return JsonResponse({"status": 1, 'invoice_total_qty':invoice_total_qty,'invoice_amount':invoice_amount
                         })
  else:
    return JsonResponse({"status": 0})  
def invoice2_delete (request) :
    if request.method == "POST":  
      id = request.POST.get("sid")
      invoice = Invoice.objects.get(pk=id)
      print(f'record to delete : {invoice}')
      invoice.delete()
      invoicedata =   Invoice.objects.filter(user=request.user, invoice_no = 0).values('id','customer','customer__name','description','invoice_date','quantity', 'price', 'amount')      

      invoice_total_qty=0
      invoice_amount=0
      for i in  invoicedata:
        invoice_total_qty += i['quantity']
        invoice_amount += i['price'] *i['quantity']      

      return JsonResponse({"status": 1, 'invoice_total_qty':invoice_total_qty,'invoice_amount':invoice_amount
                         })
    else:
      return JsonResponse({"status": 0})  
    

def search_item(request):
  print(' search-item')
# -------  category
def category_dashboard(request):
  data = Category_Sales.objects.all()
  context={'data':data, }
  return render(request,'app_invoice/category-dashboard.html',context)
def duplicate_check_category(desc):
  datarec=Category_Sales.objects.filter(product_category=desc)
  if datarec:
    return True
  else:
    return False
  

  
def category_add(request):
  categories= Category_Sales.objects.all()  
  context={'categories':categories}  
  if request.method=='POST':
    product_category = request.POST['product_category']
    if not product_category :
      messages.error(request, 'Product category is required') 
      context={'categories':categories, 'values':request.POST }
      return render(request,'app_invoice/category-add.html',context)
    if duplicate_check_category(product_category):
      messages.error(request, 'Duplicate entry, data not saved') 
    else :
      data = Category_Sales(product_category=product_category, user=request.user)
      data.save()
      messages.success(request, 'Expense entry saved successfully') 
      return redirect('app_invoice:category-dashboard')    
    
  context={'categories':categories, 'values':request.POST}
  return render(request,'app_invoice/category-add.html',context)

def category_delete(request, pk=None):
  datarec= Category_Sales.objects.get(id=pk)

  form = DeleteRecord_CategoryForm(instance =datarec)   

  if request.method=='POST':
    datarec.delete()   
    return redirect('app_invoice:category-dashboard', )
  
  context={'form':form,'datarec':datarec}
  return render(request,'app_invoice/category-delete.html',context)  
def category_update(request, pk=None):
  datarec= Category_Sales.objects.get(id=pk)

  form = UpdateRecord_CategoryForm(instance =datarec)   

  if request.method=='POST':
    form = UpdateRecord_CategoryForm(request.POST or None, instance = datarec)
    if form.is_valid():
      form.save()
      return redirect('app_invoice:category-dashboard', )
  
  context={'form':form,'datarec':datarec}
  return render(request,'app_invoice/category-update.html',context)  


# ------- master file
def duplicate_check_masterfile(item):
  datarec = ''
  datarec=MasterFile.objects.filter(itemnumber=item)

  if datarec:
    return True
  else:
    return False  
  
def masterfile_dashboard(request):
  data = MasterFile.objects.all()
  
  context={'data':data, }
  return render(request,'app_invoice/masterfile-dashboard.html',context)

def masterfile_add(request):
  categories= Category_Sales.objects.all()  
  form = Masterfile_form()
  context={'categories':categories, 'form':form}  
  if request.method=='POST':
    form=Masterfile_form(request.POST or None, request.FILES or None )
    if form.is_valid():
      saveform =form.save(commit=False)
      saveform.user = request.user
      saveform.save()
      return redirect('app_invoice:masterfile-dashboard')
    else :
      print(f'form is invalid {form.errors}')

    
  context={'categories':categories, 'form':form}  
  return render(request,'app_invoice/masterfile-add.html',context)

def masterfile_update(request, pk=None):

  datarec= MasterFile.objects.get(id=pk)

  form = UpdateRecord_MasterFileForm(instance =datarec)

  if request.method=='POST':

    form = UpdateRecord_MasterFileForm(request.POST or None, request.FILES or None, instance = datarec)
    if form.is_valid():  
      saveform=form.save(commit=False)
      saveform.user= request.user
      saveform.save()
      return redirect('app_invoice:masterfile-dashboard' )
    else:

      print(f'form is invalid update masterfile {form.errors}')

  context={'form':form,'datarec':datarec}
  return render(request,'app_invoice/masterfile-update.html',context)

def masterfile_delete(request, pk=None):
  datarec= MasterFile.objects.get(id=pk)

  form = DeleteRecord_MasterFileForm(instance =datarec)   

  if request.method=='POST':
    datarec.delete()   
    return redirect('app_invoice:masterfile-dashboard', )
  
  context={'form':form,'datarec':datarec}
  return render(request,'app_invoice/masterfile-delete.html',context)  



def sales_entry_dashboard(request):
  data = Invoice.objects.filter(user = request.user, invoice_no=0) 
  context={'data':data}
  return render(request,'app_invoice/sales-entry-dashboard.html',context)

def sales_entry_delete(request,pk=None):
  datarec= Invoice.objects.get(id=pk)
  form = DeleteRecord_SalesEntryForm(instance =datarec)   
  if request.method=='POST':
    datarec.delete()   
    return redirect('app_invoice:sales-entry', )


  context={'form':form,'datarec':datarec}
  return render(request,'app_invoice/sales-entry-delete.html',context)  

