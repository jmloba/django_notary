from django.shortcuts import render,redirect
from .models import Expense, Category
from django.contrib import messages
from app_expenses.forms import DeleteRecord_ExpenseForm,UpdateRecord_ExpenseForm


# Create your views here.
def expense_dashboard(request):
  data = Expense.objects.filter(posted=False,owner= request.user)


  context={'data':data, }
  return render(request,'app_expenses/expense-dashboard.html',context)

def expenses_add(request):
  categories= Category.objects.all()  
  context={'categories':categories}
  if request.method=='POST':
    amount = request.POST['amount']
    if not amount:
      messages.error(request, 'Amount is required') 
      context={'categories':categories, 'values':request.POST }
      return render(request,'app_expenses/expense-add.html',context)

    description = request.POST['description']
    if not description:
      messages.error(request, 'Description is required') 
      context={'categories':categories, 'values':request.POST }
      return render(request,'app_expenses/expense-add.html',context)


    mdate = request.POST['expense_date']
    if not mdate:
      messages.error(request, 'Date is required') 
      context={'categories':categories, 'values':request.POST }
      return render(request,'app_expenses/expense-add.html',context)

    category = request.POST['category']
    if not category:
      messages.error(request, 'Category is required') 
      
      context={'categories':categories, 'values':request.POST }
      return render(request,'app_expenses/expense-add.html',context)

    print(f'form value : amount : {amount}\n description : {description} \n date :{mdate}\ncategory :{category} ')

    expense_rec=Expense(
      amount=amount,
      description=description,
      date=mdate, 
      category=category,
      owner=request.user
      )
    expense_rec.save()
    
    messages.success(request, 'Expense entry saved successfully') 

    return redirect('app_expenses:expense-dashboard')

  context={'categories':categories, 'values':request.POST}
  return render(request,'app_expenses/expense-add.html',context)

def expenses_delete(request, pk=None):
  datarec= Expense.objects.get(id=pk)

  form = UpdateRecord_ExpenseForm(instance =datarec)   

  if request.method=='POST':
    datarec.delete()   
    return redirect('app_expenses:expense-dashboard', )
  
  context={'form':form,'datarec':datarec}
  return render(request,'app_expenses/expense-delete.html',context)  

def expenses_update(request, pk=None):
  datarec= Expense.objects.get(id=pk)
  form = UpdateRecord_ExpenseForm(instance =datarec)

  if request.method=='POST':

    form = UpdateRecord_ExpenseForm(request.POST or None, instance = datarec)
    if form.is_valid():  
      form.save()
      return redirect('app_expenses:expense-dashboard', )

  context={'form':form,'datarec':datarec}
  return render(request,'app_expenses/expense-update.html',context)




def create_expense_rec(request):
  pass
