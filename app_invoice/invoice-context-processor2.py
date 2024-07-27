from .models import Invoice

def contextprocessor_total_quantity(request):
  inv_total_qty = 0
  inv_total_amount = 0

  if (request.user.is_authenticated):
    invoice = Invoice.objects.filter(user = request.user, invoice_no =0)
    
    inv_total_qty=0
    inv_total_amount =0
    for item in invoice :
      inv_total_qty += item.quantity
      inv_total_amount += item.amount

    inv_total_qty+=   inv_total_qty +100
    inv_total_amount += inv_total_amount+100


  return {'inv_total_qty': inv_total_qty,'inv_total_amount':inv_total_amount}
