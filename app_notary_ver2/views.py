
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from app_notary_ver2.forms import Notary_form
from app_notary.models import Notarized_Documents
from django.template.loader import render_to_string

# Create your views here.

def notaryv2_entry_modal(request):

  notary_list=Notarized_Documents.objects.all()

  context={  'notary_list':notary_list}
  return render(request,'app_notary_ver2/notaryv2-entry-modal.html', context)


def save_notary_form(request, form ,template_name):
  # initialize data as dictionary
  data= dict()
  if request.method == 'POST':
    if form.is_valid():
      s= form.save(commit = False)
      s.user = request.user
      s.save()

      data['form_is_valid'] = True
      notary_list = Notarized_Documents.objects.all()

      data['html_notary_list']= render_to_string('app_notary_ver2/partial_notary_v2_list.html',{'notary_list':notary_list})
    else:
      data['form_is_valid'] = False

  context ={'form':form}
  data['html_form'] = render_to_string(template_name, context, request=request)
  return JsonResponse(data)

def modal_v2_notary_create(request):
  if request.method=='POST':
    form = Notary_form(request.POST or None, request.FILES or None )
  else:
    print('request is not post')
    form = Notary_form()

  return save_notary_form(request, form,'app_notary_ver2/partial_notary_v2_create.html')  

def modal_v2_notary_update(request, pk=None):
  product=get_object_or_404(Notarized_Documents,pk=pk)
  if request.method =='POST':
    form=Notary_form(request.POST or None, request.FILES or None, instance=product)
  else:
    form=Notary_form( instance=product)
  return save_notary_form(request, form,'app_notary_ver2/partial_notary_v2_update.html')  


def modal_v2_notary_delete (request, pk=None):

  notary_item =get_object_or_404(Notarized_Documents,pk=pk)
  data = dict()

  if request.method =='POST':
    notary_item.delete()

    data['form_is_valid'] = True
    notary_list = Notarized_Documents.objects.all()
    context = {'notary_list':notary_list}

    data['html_notary_list']= render_to_string('app_notary_ver2/partial_notary_v2_list.html',context)

  else:
    context={'notary_item':notary_item}
    data['html_form'] = render_to_string('app_notary_ver2/partial_notary_v2_delete.html',context, request=request)
    
  return JsonResponse(data)


    