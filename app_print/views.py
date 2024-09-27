
import subprocess
from django.shortcuts import render,HttpResponse,redirect
from app_invoice.models import Invoice, InvoiceSummary
from django.http import JsonResponse

from django.db.models import Sum, Q
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm
from reportlab.lib.pagesizes import A4
from reportlab.lib import utils
from reportlab.platypus import Frame, Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,  Preformatted, XPreformatted 
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

from .invtemplate import print_template,reference_code_print
from .forms import SearchForm
from .reportlab_passwordprotected import print_password_protected
from .reportlab_invoice_template import invoice_template



def reprint_invoice(request):
  print(f'start')
  invoice_summary = InvoiceSummary. objects.filter(invoice_no = 0)
  form = SearchForm()
  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
      invoice = request.POST.get('invoiceno')

      invoice_summary = InvoiceSummary. objects.filter(invoice_no = invoice)

      context={'form':form,'invoice_summary': invoice_summary,}
      print(f'invoice *** : {invoice}' )
      return render(request,'app_print/reprint-invoice.html' ,context ) 
    else:
      print('form is invalid')


  context={ 'form':form }
  return render(request,'app_print/reprint-invoice.html' ,context ) 

def print_invoice_now(invoice_list,pdf_path,invoice_no):
  mypath = pdf_path

  rowcount =1
  global mtotals 
  mtotals= 0.0
  y_axis = 6.0
  global  page_total 
  page_total = 0.0
  g_total = 0.0
  pageno =1
  c=canvas.Canvas(mypath, pagesize=A4)
  c.translate(inch, inch)  # x y position using inch  
  c,pageno = print_template(c,pageno,invoice_no)  
  
  for row_number, row_data in enumerate(invoice_list):
    # print_letter_heading(c)
    rowcount += 1
    page_total = print_body_data(c, row_data ,y_axis, page_total)
    y_axis -= 0.3

    if rowcount > 3 :
        print_pagetotal(c,page_total)
        g_total += page_total
        page_total = 0.0
        c.showPage()
        c.translate(inch, inch)
        c,pageno = print_template(c,pageno,invoice_no)  # load template
 
        y_axis = 6.0
        rowcount = 1
  g_total += page_total
  print_pagetotal(c,page_total)
  print_page_grand_total(c,g_total)
  c.showPage()
  c.save()
  # to open pdf
  subprocess.Popen([mypath], shell=True)

def print_pagetotal(c,page_total):
    c.setFillColor('#071952')
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,2*inch, "Page Total :")

    c.setFillColor('#884A39')
    c.drawString(2*inch,2*inch, str(page_total))

def print_page_grand_total(c, g_total):
    c.setFillColor('#071952')
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,1.7*inch, "Grand Total :")



    c.setFillColor('#fd1f1f')
    c.drawString(2*inch,1.7*inch, str(g_total))

def print_body_data(c,row_data, y_axis,page_total):
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 12)

  print(f'\n\n row data : \n {row_data}')
  mitem = row_data['itemnumber']
  mdesc = row_data['description']
  mqty =  str(row_data['quantity'])
  mprice =  str(row_data['price'])
  mamt = str(row_data['amount'])

  page_total += float(row_data['amount'])
  # mtotals +=row_data['amount']
  c.drawString(-.5*inch, y_axis * inch, mitem)
  c.drawString(1.2*inch, y_axis * inch, mdesc)
  c.drawString(4*inch, y_axis * inch, mqty)
  c.drawString(5*inch, y_axis * inch, mprice)
  c.drawString(6*inch, y_axis * inch, mamt)
  return page_total

def get_invoice_to_print(new_invoice):
  mdata = Invoice.objects.filter(invoice_no = new_invoice).values('invoice_no','itemnumber', 'description', 'quantity','price','amount')
  invoice_list= list(mdata)   
  print(f'invoice list : {invoice_list}')

  return invoice_list

def print_invoice(request,new_invoice):
  print(f'app_print print invoice routine')
  invoice_list = get_invoice_to_print(new_invoice)

  if invoice_list==None:
    return HttpResponse('Nothing to print ... app_print/print_invoice')

  
  if  invoice_list:
    mypath = 'c:/reportlab/invoice.pdf'
    print_invoice_now(invoice_list,mypath,new_invoice)

    # joven
    return redirect('app_invoice:invoice-create')
  else  :
    mypath=''
    print('nothing to print')

  context={'invoice_list':invoice_list ,'mypath':mypath  }
  return render(request,'app_print/print-invoice.html' ,context ) 

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# pass value
def reportlab(request):
  context={  }
  return render(request,'app_print/reportlab.html' ,context ) 

def reportlab_password_protected(request):
  print(f'procedure reportlab pasword protected')
  if request.method == 'POST':
    if is_ajax(request):
      name_pass  =  request.POST['name_pass']

      print(f'ajax request : name :{name_pass}')
      response = {'status':'Success', 'Message': 'ajax request - password protected'}
      return JsonResponse(response)
    else :
      response = {'status':'Success', 'Message': 'not ajax request'}
      return JsonResponse(response)
  else :
      file_password ='Mike2454'
      mypath = 'c:/reportlab/password_protected.pdf'
      if print_password_protected(request,mypath,file_password):
        subprocess.Popen([mypath], shell=True)

      name_pass  =  request.GET['mname']
      response = {'status':'not POST', 'Message': 'request is not post !!!'+name_pass}
      return JsonResponse(response)

def reportlab_invoice_template(request):
  if request.method == 'GET':
      file_password ='Mike2454'
      mypath = 'c:/reportlab/invoice_template.pdf'
      
      if invoice_template(request,mypath):
        subprocess.Popen([mypath], shell=True)

      name_pass  =  request.GET['mname']
      response = {'status':'Success', 'Message': 'request is not post !!!'+name_pass}
      return JsonResponse(response)

  


def print_invoice_ajax(request):
  if is_ajax(request):
    new_invoice = int( request.POST['new_invoice'])
    print(f'\n new invoice : {new_invoice}, {type (new_invoice)}')
    invoice_list = get_invoice_to_print(new_invoice)
    if invoice_list==None:
      print('no records')
      response = {'status':'No Value', 'Message': 'invoice not found'}
      return JsonResponse(response)
    if  invoice_list:
      mypath = 'c:/reportlab/invoice.pdf'
      print_invoice_now(invoice_list,mypath,new_invoice)
      response = {'status':'Success', 'Message': 'invoice has been printed'}
      return JsonResponse(response)
    else  :
      mypath=''
      print('nothing to print')
      response = {'status':'No Record Found', 'Message': 'No invoice found from the table'}
      return JsonResponse(response)
  


def add_all_values (qs,simple_list):
  # add all values
  myValues = list(qs.values_list())


  print(f'myValues :\n{myValues} \n\n')
  for i in myValues:
    simple_list.append(i)

  return simple_list
 
def get_tableheader(qs):
  header = qs[0].__dict__.keys()
  mheader =[]

  for  i in header:
    print(f'counter : {i}')
    if i!='_state':
      mheader.append(i)
  return mheader  

def  create_simple_table(invno):
  

  print(f'\nsum quantity : using aggregate')
  qs= Invoice.objects.filter(invoice_no=invno)
  #qs getting the total amount
  qs_sum = Invoice.objects.filter(invoice_no=invno).aggregate(Sum('quantity'))
  simple_list=[]
  simple_list.append(get_tableheader(qs))
  simple_list = add_all_values(qs,simple_list)
  print(f'\n\nsimple list : \n{simple_list}') 

def print_invoice_tabular(request):
  mypath='c:/reportlab/tabular.pdf'
  print('recordset')
  qs=Invoice.objects.filter(invoice_no =4) 
  simple_list=[]
  simple_list.append(get_tableheader(qs))
  mydata = add_all_values(qs,simple_list)
  print('------')
  print(f'simple list : \n\n {simple_list} ')

  mydoc = SimpleDocTemplate(mypath, pagesize=letter)
  
  # t=Table(mydata, rowHeights=80, repeatRows=1)
  '''setting the column width '''
  c_width=[0.5*inch,   0.5*inch, 0.75*inch,   
           .9*inch,   2.0*inch, 0.7*inch,   
           1.5*inch, 0.5*inch,   
           ]
  t=Table(mydata, rowHeights=80, repeatRows=1,colWidths=c_width)

  '''setting table style'''
  t.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.lightgreen),
    
    # '''line 2 color yellow'''
    ('BACKGROUND',(0,2),(-1,0),colors.yellow),

    # '''line 2 color blue'''
    ('BACKGROUND',(2,3),(2,4),colors.green),

    ('FONTSIZE',(0,0),(-1,-1),8)
    ],
  ))


  elements=[]
  elements.append(t)
  mydoc.build(elements)



  context={}
  return render(request,'app_print/print-invoice-tabular.html' ,context ) 
 
