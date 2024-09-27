from app_notary.models import Notarized_Documents
from django.db.models import Sum

def get_NotaryDoc_records(request):
  data=Notarized_Documents.objects.all()
  
  no_of_Records =data.count()
  

    # qs_sum =Invoice.objects.filter(user=request.user, invoice_no = new_invoice).aggregate(Sum('quantity') , Sum('amount') ) 

  qs_sum =Notarized_Documents.objects.all().aggregate( Sum('amount') ) 

  total_sales = qs_sum["amount__sum"]
  
  context={'no_of_Records': no_of_Records,'total_sales':total_sales}
  return context