
from reportlab.pdfgen import canvas  
from reportlab.lib import pdfencrypt

def print_password_protected(request, mypath,file_password):
  print(' ready to print password protected')
  pdf_with_encrypt = pdfencrypt.StandardEncryption(file_password)
  ''' without encryption'''
  # pdf=canvas.Canvas(mypath, bottomup=0)
  ''' with encryption'''
  pdf=canvas.Canvas(mypath, bottomup=0,encrypt= pdf_with_encrypt)

  pdf.drawString(10,10, "testpdf")

  pdf.showPage()
  pdf.save()



  return True