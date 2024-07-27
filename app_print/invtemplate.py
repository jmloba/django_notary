from reportlab.lib.units import inch,cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, XPreformatted
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch


def draw_line(c):
    # line
    c.setStrokeColorRGB(1, 0, 0)  # line color in red
    c.setLineWidth(1)  # line width
    c.line(-.5*inch, 7.3 * inch, 6.8 * inch, 7.3 * inch)  
def logo_draw(c):
    #  logo print ---
    c.drawImage('c:\\reportlab\\logo\\logo_red.png', -.4 * inch, 8.5 * inch, 1.5 * inch, 1.5 * inch)    
def set_canvas(c):
    c.translate(inch, inch)  

def draw_a4_borderrectangle(c):
    # draw the rectangle
    c.setLineWidth(2)
    c.setStrokeColor("black")
    c.setFillColor("lightgreen")
    c.roundRect(-.8 * inch, -.5 * inch, 7.9 * inch, 10.7 * inch, stroke=1, radius=.1)    
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


def print_pageno(c,y_axis,pageno):    
  c.setFillColor('#050C9C')
  c.setFont("Helvetica",12)
  c.drawString( 6.0*inch, y_axis * inch, 'Page No: '+str(pageno))
def reference_code_print(c,invoice_no)  :
    c.setFillColorCMYK(0, 0, 0, 89)
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,7*inch, "Reference No :")
    c.setFillColorCMYK(30, 13, 0, 0)
    c.drawString(2*inch,7*inch, str(invoice_no))    


def print_template(c , pageno,invoice_no):

    logo_draw(c)
    draw_a4_borderrectangle(c)
    draw_line(c)

    rectangle_address(c)
    # draw_watermark(c)
    import_date(c)
    print_table_header(c,6.3)
    print_pageno(c,7.5,pageno)
    reference_code_print(c,invoice_no)
 
    pageno+=1
    return c,pageno  