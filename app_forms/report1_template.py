from reportlab.lib.units import inch,cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, XPreformatted
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor



def logo_draw(c):
    #  logo print ---
    x1 = -.5
    y1 = 9.5
    x2= 1.0
    y2= 1.0
    c.drawImage('c:\\reportlab\\logo\\logo_red.png', x1 * inch, y1 * inch, x2 * inch, y2 * inch)    
def set_canvas(c):
    c.translate(inch, inch)  

def draw_a4_borderrectangle(c):
  ''' main border
  '''
  c.setLineWidth(.5)
  c.setStrokeColor("black")
  c.setStrokeColor(HexColor('#D0B8A8'))
  c.setFillColor("lightgreen")
  # c.roundRect(-.8 * inch, -.5 * inch, 7.9 * inch, 10.7 * inch, stroke=1, radius=7)    
  ''' table border'''
  # table border

  x1 = -0.8
  y1 = 1.0


  x2 = 7.8
  y2 = 8.0
  c.roundRect( x1 * inch, y1 * inch, x2 * inch, y2 * inch, stroke=1, radius=7)

def draw_line(c,x1,y1,x2,y2):
    # line
  # c.setStrokeColorRGB(1, 0, 0)  # line color in red
  c.setStrokeColor(HexColor('#D0B8A8'))
  c.setLineWidth(1)  # line width
  c.line(x1 *inch, y1 * inch, x2 * inch, y2 * inch)   

def import_date(c):
    c.setFont("Helvetica", 10)
    c.setFillColorCMYK(27, 2, 5, 3)  # font color
    from datetime import date
    inv_date = date.today().strftime('%d-%b-%Y')
    str_date = "Date"
    c.drawString(2.1*inch,9.8*inch,str_date+": "+inv_date)    


def rectangle_address(c):
    c.setLineWidth(3)
    c.setStrokeColor("lightblue")
    c.setFillColor("lightyellow")
    c.roundRect(2*inch, 8 * inch, 4.8*inch, 2.0 * inch, fill=1, stroke=1, radius=.1*inch)   
def print_table_header(c,y_axis):    
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 14)
  c.drawString( -.5  * inch, y_axis * inch, 'Item #')
  c.drawString( 1.2  * inch, y_axis * inch, 'Description')
  c.drawString( 3.75 * inch, y_axis * inch, 'Quantity')
  c.drawString( 5.0  * inch, y_axis * inch, 'Price')
  c.drawString( 6    * inch, y_axis * inch, 'Amount')


def print_pageno(c,y_axis,pageno,var_color_black):    
  c.setFillColor(var_color_black)
  c.setFont("Helvetica",10)
  c.drawString( 6.0*inch, y_axis * inch, 'Page No: '+str(pageno))



def reference_code_print(c,invoice_no)  :
    c.setFillColorCMYK(0, 0, 0, 89)
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,7*inch, "Reference No :")
    c.setFillColorCMYK(30, 13, 0, 0)
    c.drawString(2*inch,7*inch, str(invoice_no))

def print_heading(c):
  c.setFillColorCMYK(1,0,0,89)
  c.setFillColor('#000000') # black
  c.setFont("Helvetica", 8)   
  posted_serial='Posted(Reference)'
  name='Name'
  category='Category'
  x1= -.4
  y1= 8.85
  c.drawString(x1*inch, y1 * inch, posted_serial)
  x1= .8
  c.drawString(x1*inch, y1 * inch, name)   
  x1= 2.1
  c.drawString(x1*inch, y1 * inch, category)   


  x1= -.4
  y1 -= .3
  c.setFillColor('#229799') 
  c.drawRightString(1.8*inch, y1 * inch, 'Book No')   
  c.drawRightString(2.55*inch, y1 * inch, 'Page No')   
  c.drawRightString(3.3*inch, y1 * inch, 'Record No')     
  c.setFillColor('#1230AE')   # dark blue
  c.drawRightString(4.6*inch, y1 * inch, 'Amount')   
  c.drawRightString(5.4*inch, y1 * inch, 'Tax')   
  c.drawRightString(6.5*inch, y1 * inch, 'Total Amount')   

def print_template(c , pageno, date_filtered,var_color_black):

    logo_draw(c)
    draw_a4_borderrectangle(c)
    print_heading(c)
    x1 = -0.8
    y1 = 8.5
    x2 = 7.0
    y2 = 8.5   
    draw_line(c,x1,y1,x2,y2)
    x1 = -0.8
    y1 = 1.5
    x2 = 7.0
    y2 = 1.5   
    draw_line(c,x1,y1,x2,y2)

    # rectangle_address(c)
    # # draw_watermark(c)
    # import_date(c)
    # print_table_header(c,6.3)
    y_axis=9.1
    print_pageno(c, y_axis, pageno,var_color_black)
    print_date_filtered(c, y_axis, pageno,date_filtered,var_color_black)    
    # reference_code_print(c)
 
    pageno+=1
    return c,pageno  


def print_date_filtered(c,y_axis,pageno,date_filtered,var_color_black):    
  c.setFillColor(var_color_black)
  c.setFont("Helvetica",10)
  c.drawString( -.5*inch, y_axis * inch, date_filtered)