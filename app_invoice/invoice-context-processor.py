from .models import Invoice

def total_quantity(request):
  invoice_total_qty=0
  invoice_amount =0

  if (request.user.is_authenticated):
    invoice = Invoice.objects.filter(user = request.user, invoice_no =0)
    
    invoice_total_qty=0
    invoice_amount =0
    for item in invoice :
      invoice_total_qty += item.quantity
      invoice_amount += item.amount


  return {'invoice_total_qty': invoice_total_qty,'invoice_amount':invoice_amount}
