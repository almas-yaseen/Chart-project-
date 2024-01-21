from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .import views
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
import json 
from django.views.decorators.cache import never_cache
from django.http import JsonResponse


# Create your views here.
def search_expenses(request):
    try:
        if request.method == "POST":
            search_str = json.loads(request.body).get('searchText')
            
            expenses = Expense.objects.filter(
                amount__istartswith=search_str,
                owner=request.user
            ) | Expense.objects.filter(
                date__istartswith=search_str,
                owner=request.user
            ) | Expense.objects.filter(
                description__icontains=search_str,
                owner=request.user
            ) | Expense.objects.filter(
                category__icontains=search_str,
                owner=request.user
            )
            
            data = expenses.values()
            return JsonResponse(list(data), safe=False)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)





@login_required(login_url='/authentication/login')
@never_cache
def index(request):
    categories = Category.objects.all()
    expense = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expense,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories':categories,
        'expense':expense,
        'page_obj':page_obj,
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
    categories = Category.objects.all()
    context = {
        'expense':expense,
        'values':expense,
        'categories':categories,  
    }
       
    

    if request.method=="POST":
        print("akljklasdjksad")
        amount = request.POST['amount']
        description = request.POST['description']
        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'expenses/edit-expense.html',context)
        
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']
        
        
        if not description:
            messages.error(request,'Amount is required')
            return render(request,'expenses/edit-expense.html',context)
        
        
        expense.owner = request.user
        expense.amount = amount 
        expense.date = date
        expense.category = category
        expense.description = description
        expense.save()
        messages.success(request,'Expense updated successfully')
    return render(request,'expenses/edit-expense.html',context)




def delete_expense(request,id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('expenses')