from reportlab.lib.units import inch,cm

def print_logo(c,x,y):    
  image='c:\\reportlab\\logo\\logo_red.png'
  xloc = x*inch
  yloc = y*inch
  c.drawImage(image, xloc,yloc,1.8*cm,1.8*cm)

def print_text(c,mtext,x,y) : 
  c.drawString(x*inch,y*inch,mtext)
  



def print_rectangle(c, x1,y1,x2,y2) : 
  c.setLineWidth(1)
  c.rect(x1*inch,y1*inch, x2*inch,y2*inch, fill=0 )
def  print_letter_heading(c):
  # rectangle
  c.setStrokeColorCMYK(100,90,0,0,)
  print_rectangle(c,-.5,9,7,1 )
  print_logo(c,-.3,9.1)
  c.setFillColor('blue')
  c.setFillColor('#995887')
  c.setFont('Helvetica',30)
  print_text(c,'Company XYZ',2,9.65)

def print_heading(c): 
  c.setLineWidth(3)
  c.setStrokeColor('blue')
  c.setFillColorCMYK(49,13,29,12)
  c.rect(.5*inch,5*inch, 6*inch,2*inch, fill=0 )

def print_line(c, x1,y1,x2,y2,line_width) : 
  c.setLineWidth(line_width)
  c.setFillColorRGB(1,0,0)  # fill color red
  
  c.line(x1*inch,y1*inch, x2*inch,y2*inch )


def print_watermark(c):
  # watermark
  c.setFillColorCMYK(0,0,0,.08)  # fill color red
  c.setFont('Helvetica',100)
  c.rotate(5)
  c.drawString(3*inch,2*inch,'watermark')


def print_a_line (c): 
  # draw a line
  c.setStrokeColorRGB(1,0,0)# line color in red
  line_width=2
  print_line(c,1,8,8,8,line_width)  


  