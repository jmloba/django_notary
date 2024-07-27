from app_invoice.models import Invoice

def get_invoice_list(invoice_no):
  mydata=Invoice.objects.filter()