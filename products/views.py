from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .import views
from django.contrib import messages
from .models import *
from django.views.decorators.cache import never_cache

# Create your views here.

@login_required(login_url='/authentication/login')
@never_cache
def index(request):
    categories = Category.objects.all()
    expense = Expense.objects.filter(owner=request.user)
    context = {
        'categories':categories,
        'expense':expense,
    }
    return render(request,'expenses/index.html',context)


def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'values':request.POST
    }
    if request.method=="POST":
        print("akljklasdjksad")
        amount = request.POST['amount']
        description = request.POST['description']
        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'expenses/add_expense.html',context)
        
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']
        
        
        if not description:
            messages.error(request,'Amount is required')
            return render(request,'expenses/add_expense.html',context)
        
        Expense.objects.create(owner=request.user,amount=amount,date=date,category=category,description=description)
        
        messages.success(request,'Expense saved successfully')
        
        return redirect('expenses')
            
    
    
    return render(request,'expenses/add_expense.html',context)






def expense_edit(request,id):
    expense  =Expense.objects.get(id=id)
    context = {
        'expense':expense,
        'values':expense,
        
    }
    if request.method=="GET":
        return render(request,'expenses/edit-expense.html',context)
    
    else:
        messages.info(request,'Handling post form')
        return render(request,'expenses/edit-expense.html',context)
        
        
  