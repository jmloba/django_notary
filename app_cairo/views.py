
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, FileResponse,HttpResponse
from app_cairo.models import Product
from app_cairo.forms import ProductForm
from django.template.loader import render_to_string



def product_list(request):
  products = Product.objects.all()
  context={'products':products}
  return render(request,'app_cairo/main-entry.html', context)

def save_product_form(request, form ,template_name):
  # initialize data as dictionary
  data= dict()
  if request.method == 'POST':
    print(f'request us post save product')
    if form.is_valid():
      form.save()
      data['form_is_valid'] = True

      products=Product.objects.all()

      data['html_product_list']= render_to_string('app_cairo/partial_product_list.html',{'products':products})
    else:
      data['form_is_valid'] = False

  context ={'form':form}
  data['html_form'] = render_to_string(template_name, context, request=request)
  return JsonResponse(data)

def product_create(request):
  if request.method=='POST':
    form = ProductForm(request.POST)
  else:
    print('request is not post')
    form = ProductForm()

  return save_product_form(request, form,'app_cairo/partial_product_create.html')  

def product_update(request,pk=None):
  product=get_object_or_404(Product,pk=pk)
  if request.method =='POST':
    form=ProductForm(request.POST, instance=product)
  else:
    form=ProductForm( instance=product)
  return save_product_form(request, form,'app_cairo/partial_product_update.html')  

def product_delete(request,pk=None):
  product=get_object_or_404(Product,pk=pk)
  data = dict()
  
  if request.method =='POST':
    product.delete()

    data['form_is_valid'] = True
    products = Product.objects.all()
    
    data['html_product_list']= render_to_string('app_cairo/partial_product_list.html',{'products':products})
    
  else:
    context={'product':product}
    
    data['html_form'] = render_to_string('app_cairo/partial_product_delete.html',context, request=request)

    
  return JsonResponse(data)







