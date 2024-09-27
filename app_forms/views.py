from django.shortcuts import get_object_or_404, render,redirect
from app_notary.models import Notarized_Documents, Notary_Category, File_Serials, Notary_Posting
from app_import.models import Phil_City,Phil_Province_Towns
from app_invoice.models import Tax

from app_forms.forms import CreateRecordNotaryForm,UpdateRecordNotaryForm, CreateRecordCategoryForm, UpdateRecordCategoryForm,Date_filter, Sampleform


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import simplejson as json
from app_notary.utils import generate_posting_refno
from datetime import datetime
import subprocess


from django.contrib import messages


from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm
from reportlab.lib.pagesizes import A4
from reportlab.lib import utils
from reportlab.platypus import Frame, Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,  Preformatted, XPreformatted 
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from .report1_template import print_template
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
''' category'''

@login_required(login_url='app_accounts:login-view')
def category_dashboard(request):
  data=Notary_Category.objects.all()
  form = CreateRecordCategoryForm()

  context={'data':data, }
  return render(request,'app_forms/category-dashboard.html',context)

@login_required(login_url='app_accounts:login-view')
def create_record_category(request):
  form = CreateRecordCategoryForm()
  if request.method=='POST':
    form = CreateRecordCategoryForm(request.POST or None)
    if form.is_valid():
      s=form.save(commit=False)
      s.user = request.user 
      s.save()
      
      data=Notary_Category.objects.all()
      context={'data':data, }

      return redirect('app_forms:category-dashboard', )
    else:
      return redirect('app_forms:category-dashboard' )
      print(f'create_record form is not valid ')
  context={'form':form, }
  return render(request,'app_forms/create-record-category.html',context)

@login_required(login_url='app_accounts:login-view')
def update_category_record(request, pk=None):
  datarec= Notary_Category.objects.get(id=pk)
  form = UpdateRecordCategoryForm(instance =datarec)

  if request.method=='POST':

    form = UpdateRecordCategoryForm(request.POST or None,  instance = datarec)
    if form.is_valid():  
      form.save()
      return redirect('app_forms:category-dashboard', )

  context={'form':form,'datarec':datarec}
  return render(request,'app_forms/update-category-record.html',context)

@login_required(login_url='app_accounts:login-view')  
def delete_category_record(request, pk=None):

  datarec= Notary_Category.objects.get(id=pk)
  form = UpdateRecordCategoryForm(instance =datarec)   

  if request.method=='POST':

    datarec.delete()   
    return redirect('app_forms:category-dashboard', )


  context={'form':form,'datarec':datarec}
  return render(request,'app_forms/delete-category-record.html',context)

''' notary dashboard'''

@login_required(login_url='app_accounts:login-view')
def dashboard(request):
  data=Notarized_Documents.objects.filter( user = request.user, is_posted = False).order_by('created')


  form = CreateRecordNotaryForm()

  context={'data':data, }
  return render(request,'app_forms/dashboard.html',context)

def get_tax_values(request,form):
  amount = int(form['amount'].value())
  get_tax = Tax.objects.filter(is_active= True)
  mtotal_tax_amount =0
  tax_dict = {}
  for i in get_tax:
    tax_type = i.tax_type
    tax_percentage = i.tax_percentage
    tax_amount = round((tax_percentage * amount)/100,2)
    mtotal_tax_amount+=tax_amount
    print (f'\ntax type :{tax_type},\ntax percentage :{tax_percentage}, \ntax amount:{tax_amount},\nmtotal_tax_amount:{mtotal_tax_amount}')
    tax_dict.update({tax_type:{str(tax_percentage):tax_amount}})
  tax =0
  # for key in  tax_dict.values():
  #   for x in key.values():
  #     tax = tax +x
  tax=sum(x for  key in tax_dict.values() for x in key.values())   
  gtotal = amount+ tax
  print(f'saving 2 : tax : {tax},  mtotal_tax_amount:{mtotal_tax_amount}, amount+tax :{gtotal}')
  return mtotal_tax_amount, gtotal, tax_dict

def save_1(request,form):
  amount = int(form['amount'].value())

  get_tax = Tax.objects.filter(is_active= True)
  mtotal_tax_amount =0
  tax_dict = {}
  for i in get_tax:
    tax_type = i.tax_type
    tax_percentage = i.tax_percentage
    tax_amount = round((tax_percentage * amount)/100,2)
    mtotal_tax_amount+=tax_amount
    print (f'\ntax type :{tax_type},\ntax percentage :{tax_percentage}, \ntax amount:{tax_amount},\nmtotal_tax_amount:{mtotal_tax_amount}')
    tax_dict.update({tax_type:{str(tax_percentage):tax_amount}})

  tax =0
  # for key in  tax_dict.values():
  #   for x in key.values():
  #     tax = tax +x
  tax=sum(x for  key in tax_dict.values() for x in key.values())    

  print(f'\n total tax :{tax}')
  s=form.save(commit=False)
  s.user = request.user 
  s.total_tax_amount =mtotal_tax_amount
  s.total_tax_amount =tax
  s.tax_data = json.dumps(tax_dict)
  s.total_amount = tax + amount
  s.save()

def save_2(request,form):  
  newrec = Notarized_Documents()
  newrec.user= request.user
  # newrec.category= form.cleaned_data['category.doc_category']
  newrec.firstname= form.cleaned_data['firstname']
  newrec.lastname= form.cleaned_data['lastname']
  newrec.category = form.cleaned_data['category']

  newrec.address= form.cleaned_data['address']
  newrec.bookno= form.cleaned_data['bookno']
  newrec.pageno= form.cleaned_data['pageno']
  newrec.recordno= form.cleaned_data['recordno']
  newrec.amount= form.cleaned_data['amount']
  newrec.or_number= form.cleaned_data['or_number']
  newrec.myimage= form.cleaned_data['myimage']
  newrec.myfile= form.cleaned_data['myfile']
  mtotal_tax_amount, gtotal , tax_dict =get_tax_values(request,form)
  newrec.user = request.user 
  newrec.total_tax_amount =mtotal_tax_amount
  newrec.tax_data = json.dumps(tax_dict)
  newrec.total_amount = gtotal
  newrec.save()

@login_required(login_url='app_accounts:login-view')
def create_record(request):
  form = CreateRecordNotaryForm()
  print('create record entry')

  if request.method=='POST':
    form = CreateRecordNotaryForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
      # save_1(request, form)
      save_2(request, form)
      data=Notarized_Documents.objects.all()
      context={'data':data, }

      return redirect('app_forms:dashboard', )
    else:
      print(f'Creating Record  error: {form.errors}' )

      return redirect('app_forms:dashboard' )
      

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

''' province / town dashboard'''
@login_required(login_url='app_accounts:login-view')
def provtown_dashboard(request):
  data=Phil_Province_Towns.objects.all()
  form = CreateRecordCategoryForm()

  context={'data':data, }
  return render(request,'app_forms/category-dashboard.html',context)


def get_from_file_serial(mkey=None):
  qs =File_Serials.objects.filter(serial_name=mkey).values('next_serial_number')
  prev_val = qs[0]['next_serial_number']
  print(f'prev_val  :   {type(prev_val)} , {prev_val}'  )

  File_Serials.objects.filter(serial_name=mkey).update(next_serial_number=prev_val+1)

  newval =File_Serials.objects.filter(serial_name=mkey).values('next_serial_number')
  
  print(f' prev_val{prev_val}, newval: {newval}')
  return prev_val

@login_required(login_url='app_accounts:login-view')

def post_entries(request):
  if request.user.user.post_notary_access:
    data= Notarized_Documents.objects.filter(is_posted = False)

    data= Notarized_Documents.objects.all()

    if request.method == 'POST':

      id_list = request.POST.getlist('boxes')
      print(f'id_list : {id_list}')

      mserial = get_from_file_serial('Notary Posting Serial')
      unique_key = generate_posting_refno(mserial)
      
      posting_datetime = datetime.now()

      t_amount = 0.0 
      total_amount = 0.0 
      t_tax =0.0
      gtotal = 0.0
      count = 0

      print(f'\n\n*** looping in id_list\n') 

      for x in id_list:
        count += 1
        # get amount
        mdata = Notarized_Documents.objects.filter(pk=int(x)).values()
        for item in mdata :
          t_amount += float(item['amount'])
          t_tax += float(item['total_tax_amount'])
          gtotal += float(item['total_amount'])

        # update record        
        mdata = Notarized_Documents.objects.filter(pk=int(x)).update(is_posted=True,date_posted = posting_datetime, posted_serial=unique_key)

      # saving to Notary_Posting
      newrec = Notary_Posting.objects.create(
      user = request.user,
      amount = t_amount,
      tax = t_tax,
      total_amount = gtotal,      
      posted_serial = unique_key,
              
      )
      messages.success(request, 'items are now posted')   
      return redirect('app_forms:post-entries', )
    else:
      context={'data':data, }
      return render(request,'app_forms/post-entries.html',context)
  else:
    messages.success(request, 'You are not allowed to Post an Item')    
    return redirect('app_forms:dashboard', )
  
def get_data_to_print(date1,date2):
  mdata = Notarized_Documents.objects.filter(created__range=[date1, date2]).values('posted_serial','date_posted', 'firstname', 'lastname','bookno','pageno','recordno','amount','total_tax_amount','total_amount','category__doc_category' )
  data_list= list(mdata)   
  print(f'data list : {data_list}')

  return data_list

def print_template_now(c,pageno,date_filtered,var_color_black):
        c.showPage()
        c.translate(inch, inch)
        c,pageno = print_template(c,pageno,date_filtered,var_color_black)  # load template

def print_data_now(mypath,dataprint, date_filtered):
  print(f'\n\n\n data to print : {dataprint}')
  rowcount =1
  global mtotals 
  mtotals= 0.0
  y_axis = 8.3
  global  page_total 
  page_amount = 0.00
  page_total = 0.00
  tax_page_total = 0.00

  tax_grand_total =0.0
  g_amount =0.0
  g_total = 0.0
  g_tax_total=0.0
  pageno =1
  # c=canvas.Canvas(mypath, pagesize=A4, bottomup=0)
  c=canvas.Canvas(mypath, pagesize=A4)

  c.translate(inch, inch)  # x y position using inch  
  var_color_black = '#343131'
  c,pageno = print_template(c,pageno,date_filtered, var_color_black)  
  print(f'before reading dataprint')
  newpage_flag = True
  
  for row_number, row_data in enumerate(dataprint):
    # print_letter_heading(c)
    if newpage_flag == False:
        c.showPage()
        c.translate(inch, inch)
        c,pageno = print_template(c,pageno,date_filtered,var_color_black)  # load template
    rowcount += 1
    
    tax_page_total,page_total, page_amount, y_axis = print_body_data(c, row_data ,y_axis, page_amount, page_total,tax_page_total)
    y_axis -= 0.3
    
    newpage_flag = True


    if rowcount >4 :
        print_pagetotal(c,page_total,y_axis,tax_page_total, page_amount)
        g_total += page_total
        g_tax_total += tax_page_total
        g_amount +=page_amount

        page_amount = 0.00
        page_total = 0.0
        tax_page_total=0.0

        # c.showPage()
        # c.translate(inch, inch)
        # c,pageno = print_template(c,pageno,date_filtered,var_color_black)  # load template

        y_axis = 8.3
        rowcount = 1
        newpage_flag = False

  g_amount += page_amount
  g_total += page_total
  g_tax_total += tax_page_total
  if newpage_flag==True:

    print_pagetotal(c,page_total,y_axis,tax_page_total, page_amount)
  gtaxtotal_str=  str("%.2f" % g_tax_total)  

  print(f'Grand Total : \n , G Amount : {g_amount}\n GTotal Tax :{gtaxtotal_str} \n, G Total : {g_total} ')  

  print_page_grand_total(c,y_axis,g_amount,g_total, g_tax_total) 
  c.showPage()
  c.save()

  # to open pdf
  subprocess.Popen([mypath], shell=True)  

def print_data_now_xxx(mypath,dataprint, date_filtered):
  print(f'\n\n\n data to print : {dataprint}')
  rowcount =1
  global mtotals 
  mtotals= 0.0
  y_axis = 8.3
  global  page_total 
  page_amount = 0.0
  page_total = 0.00
  tax_page_total = 0.00
  tax_grand_total =0.0
  g_total = 0.0
  g_tax_total=0.0
  pageno =1
  # c=canvas.Canvas(mypath, pagesize=A4, bottomup=0)
  c=canvas.Canvas(mypath, pagesize=A4)

  c.translate(inch, inch)  # x y position using inch  
  var_color_black = '#343131'
  c,pageno = print_template(c,pageno,date_filtered, var_color_black)  
  print(f'before reading dataprint')
  
  for row_number, row_data in enumerate(dataprint):
    # print_letter_heading(c)
    rowcount += 1
    tax_page_total,page_total, page_amount, y_axis = print_body_data(c, row_data ,y_axis, page_amount, page_total,tax_page_total)
    y_axis -= 0.3


    if rowcount >8 :
        print_pagetotal(c,page_total,y_axis,tax_page_total, page_amount)
        g_total += page_total
        g_tax_total += tax_page_total


        page_total = 0.0
        tax_page_total=0.0
        c.showPage()
        c.translate(inch, inch)
        c,pageno = print_template(c,pageno,date_filtered,var_color_black)  # load template
        y_axis = 8.3
        rowcount = 1

  g_total += page_total
  g_tax_total += tax_page_total
  print_pagetotal(c,page_total,y_axis,tax_page_total, page_amount)
  print_page_grand_total(c,g_total,y_axis, g_tax_total)
  c.showPage()
  c.save()

  # to open pdf
  subprocess.Popen([mypath], shell=True)  

def print_pagetotal(c,page_total,y_axis,tax_page_total, page_amount):
    c.setFont("Helvetica",9)
    c.setFillColor('#7D5E3F')   # dark brown
    c.drawString(-.5*inch, y_axis*inch, "Page Totals :")

    x_axis=4.6   # tax total per page
    c.drawRightString(x_axis*inch, y_axis*inch,  str("%.2f" % page_amount))


    x_axis=5.4   # tax total per page
    c.drawRightString(x_axis*inch, y_axis*inch,  str("%.2f" % tax_page_total))

    x_axis=6.5   # total amount   per page 
    c.drawRightString(x_axis*inch, y_axis*inch,  str("%.2f" % page_total))

def print_page_grand_total(c, y_axis,g_amount, g_total, g_tax_total):
    y_axis=1.3
    c.setFillColor('#fd1f1f') # red
    c.setFont("Helvetica", 10)

    c.drawString(-.5*inch,y_axis*inch, "Grand Totals:")
    c.drawRightString( 4.6 * inch , y_axis*inch, str(g_amount))
    c.drawRightString( 5.3 * inch , y_axis*inch,   str("%.2f" % g_tax_total)  )
    c.drawRightString( 6.5 * inch , y_axis*inch, str(g_total))

def print_body_data(c,row_data, y_axis, page_amount,  page_total,tax_page_total):
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 8)
  '''
    print(f'\n\n row data : \n {row_data}')
  '''
  posted_serial = row_data['posted_serial']
  name= row_data['firstname'] + ' ' +row_data['lastname']
  category = row_data['category__doc_category']
  bookno = str(row_data['bookno'])
  pageno = str(row_data['pageno'])
  recordno = str(row_data['recordno'])
  
  amount = str("%.2f" % row_data["amount"])
  total_tax =  str("%.2f" % row_data["total_tax_amount"])
  # total_amount = str(row_data['total_amount'])
  total_amount = str("%.2f" % row_data["total_amount"])

  page_amount += float(row_data['amount'])
  page_total += float(row_data['total_amount'])
  tax_page_total += float(row_data['total_tax_amount'])


  # mtotals +=row_data['amount']
  c.drawString(-.5*inch, y_axis * inch, posted_serial)
  c.drawString(.8*inch, y_axis * inch, name)
  c.drawString(2.1*inch, y_axis * inch, category)
  # second line
  y_axis -= .3
  c.setFillColor('#229799') 
  c.drawRightString(1.6*inch, y_axis * inch, bookno)
  c.drawRightString(2.35*inch, y_axis * inch, pageno)
  c.drawRightString(3.0*inch, y_axis * inch, recordno)
  c.setFillColor('#1230AE')   # dark blue
  c.drawRightString(4.6*inch, y_axis * inch, amount)
  c.drawRightString(5.4*inch, y_axis * inch, total_tax)
  c.drawRightString(6.5*inch, y_axis * inch, total_amount)
  return tax_page_total,page_total,page_amount, y_axis


def sales_report_posted(request):
  if request.method=='POST':
    
    date1 = request.POST.get('from_date')
    date2 = request.POST.get('to_date')
    print(f' type  date1 : {type(date1)} \ndate1 : {date1}, type date2 {type(date2)} date2 :{date2}')
    # Filter date
    data =Notarized_Documents.objects.filter(created__range=[date1, date2])
    date_filtered = f'Report From: {date1}  To: {date2} '


    dataprint=get_data_to_print(date1,date2)
    #print filtered data
    if dataprint:
       mypath = 'c:/reportlab/invoice.pdf'
       print_data_now(mypath,dataprint,date_filtered)


    context={'data':data}
    # return render(request,'app_forms/sales-report-1.html',context)

    return redirect('app_forms:sales-report-posted')

  else:  
    data=Notarized_Documents.objects.filter(  is_posted = True)
    data=Notarized_Documents.objects.all()
    form = Date_filter()    
    print('request method isnot post')

  context={'data':data,'form':form , }
  return render(request,'app_forms/sales-report-posted.html',context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def print_posted_filter(request):
  print(f'calling print print_posted_filter---\n\n\n')
  if request.method == 'POST':
    if is_ajax(request):
      data  =  request.POST['passed_data']

      print(f'passed value data:{data}')
      response = {'status':'Success', 'Message': 'ajax request'}
      return JsonResponse(response)
    else :
      response = {'status':'Success', 'Message': 'not ajax request'}
      return JsonResponse(response)
  else :
    response = {'status':'not POST', 'Message': 'request is not post !!!'}
    return JsonResponse(response)   

