from reportlab.pdfgen import canvas  
from reportlab.lib import pdfencrypt, colors
from reportlab.lib.units import inch, cm
from reportlab.rl_config import defaultPageSize
from reportlab.lib.pagesizes import A4
from app_invoice.models import Invoice, InvoiceSummary
def draw_ellipse(c):
  

  c.setFillColor(colors.beige)
  c.setStrokeColor('#F19ED2')
  c.ellipse(4,11,100,500, stroke = 1, fill = 1,)


def draw_circle(c):
  c.setFillColor(colors.beige)
  c.circle(60,100, 25 , stroke=1, fill= 1)

def draw_rectangle_main(c,x1,y1,x2,y2,line_width):
  c.setLineWidth(line_width)
  c.setStrokeColor('blue')
  c.setFillColor('#EAFDFC')

  c.roundRect(x1 * inch, y1 * inch, x2* inch,y2*inch, radius=.1*inch, fill =0,  stroke=1, )      

def draw_rectangle_heading(c,x1,y1,x2,y2,line_width):
  c.setLineWidth(line_width)
  c.setStrokeColor('gray')
  c.setFillColor('#FBF1D3')

  c.roundRect(x1*inch, y1*inch, x2*inch, y2*inch, radius=.1*inch, fill =1,  stroke=1, )  

def draw_rectangle_footer(c,x1,y1,x2,y2,line_width):
  c.setLineWidth(line_width)
  c.setStrokeColor('#A79277')
  c.setFillColor('#F1F1F1')
  c.roundRect(x1*inch, y1*inch, x2*inch, y2*inch, radius=.1*inch, fill =1,  stroke=1, )    

def draw_rectangle_col_header(c,x1,y1,x2,y2,line_width):
  c.setLineWidth(line_width)
  c.setStrokeColor('#A79277')
  c.setFillColor('#B9F3FC')
  c.roundRect(x1*inch, y1*inch, x2*inch, y2*inch, radius=.1*inch, fill =1,  stroke=1, )     

def draw_header_text(c,pageno,invoice_no,y_axis):  
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 10)  
  c.drawString( -.5  * inch, y_axis * inch, 'Item #')
  c.drawString( 1.2  * inch, y_axis * inch, 'Description')
  c.drawString( 3.75 * inch, y_axis * inch, 'Quantity')
  c.drawString( 5.0  * inch, y_axis * inch, 'Price')
  c.drawString( 6    * inch, y_axis * inch, 'Amount')  

def draw_line(c):
    # line
    c.setStrokeColorRGB(1, 0, 0)  # line color in red
    c.setLineWidth(1)  # line width
    c.line(-.5*inch, 7.3 * inch, 6.8 * inch, 7.3 * inch)  
def print_page(c,x,y,pageno)  : 
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 10)  
  c.drawString( x * inch, y * inch, 'Page No:'+str(pageno))
  pageno+=1
  

def print_template_now(c,pageno,invoice_no):
  draw_rectangle_main(c,  x1=-.8,y1 =-.8,x2=7.5,y2=11,line_width=.005*inch)
  draw_rectangle_heading(c,  x1=3, y1 =-.5, x2 =3.6 , y2=1.7 ,line_width=.5)
  draw_rectangle_footer(c,  x1=-.7, y1 =9.4, x2 =7.3 , y2=.7 ,line_width=.5)
  draw_rectangle_col_header(c,  x1=-.7, y1 =1.4, x2 =7.3 , y2=.4 ,line_width=.5)

  print_page(c,x=-0.5,y=1.3, pageno=pageno)
  # draw_line(c)
  y_axis=1.7
  draw_header_text(c,pageno,invoice_no, y_axis)

 


def get_invoice_to_print(new_invoice):
  mdata = Invoice.objects.filter(invoice_no = new_invoice).values('invoice_no','itemnumber', 'description', 'quantity','price','amount')
  invoice_list= list(mdata)   
  print(f'invoice list : {invoice_list}')
  return invoice_list

def print_body_data(c,row_data, y_axis,page_total):
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 10)

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
def print_pagetotal(c,page_total):
    c.setFillColor('#071952')
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,9.65*inch, "Page Total :")

    c.setFillColor('#884A39')
    c.drawString(2*inch,9.65*inch, str(page_total))
def print_page_grand_total(c, g_total):
    c.setFillColor('#071952')
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,9.9*inch, "Grand Total :")



    c.setFillColor('#fd1f1f')
    c.drawString(2*inch,9.9*inch, str(g_total))   
def pdf_annotations(c):
  c.setAuthor('joven')
  c.setTitle('Invoice')
  c.setSubject('Invoice Subject')
  c.setCreator('python sample project')



def invoice_template(request, mypath):
  file_password ='Mike2454'
  pdf_with_encrypt = pdfencrypt.StandardEncryption(file_password)
  # c=canvas.Canvas(mypath, bottomup=0, pagesize=A4 , encrypt=pdf_with_encrypt)
  c=canvas.Canvas(mypath, bottomup=0, pagesize=A4  )

  pdf_annotations(c)
  

  c.translate(inch, inch)
  # get data
  new_invoice = 32
  invoice_list = get_invoice_to_print(new_invoice)
  global pageno
  pageno =1
  rowcount = 0
  page_total = 0.00
  global g_total  
  g_total =0.00
  y_axis =2
  print_template_now(c,pageno,new_invoice)  # load template
  for row_number, row_data in enumerate(invoice_list):
    # print_letter_heading(c)
    rowcount += 1
    
    page_total = print_body_data(c, row_data ,y_axis, page_total)
    
    y_axis += 0.3

    if rowcount >= 3 :
        print_pagetotal(c,page_total)
        pageno+=1
        g_total += page_total
        page_total = 0.0
        
  
        c.showPage()
        c.translate(inch, inch)
        print_template_now(c,pageno,new_invoice)  # load template
 
        y_axis = 2.0
        rowcount = 0
  print_pagetotal(c,page_total)
  g_total += page_total  
  print_page_grand_total(c,g_total)
  c.showPage()
  c.save()

   

  return True