from django.shortcuts import render,redirect
from .models import userincome,Source
from django.core.paginator import Paginator
from userpreference.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    categories = Source.objects.all()
    income =userincome.objects.filter(owner=request.user)
    paginator = Paginator(income,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    currency = UserPreference.objects.get(user=request.user).currency
    print("Page Object:", page_obj)
    context = {
        'income':income,
        'page_obj':page_obj,
        'currency':currency,
    }
    return render(request,'income/index.html',context)




@login_required(login_url='/authentication/login')
def add_income(request):
    sources = Source.objects.all()
    context = {
        
        'sources':sources,
        'values':request.POST
    }
    if request.method=="POST":
        print("akljklasdjksad")
        amount = request.POST['amount']
        description = request.POST['description']
        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'income/add_income.html',context)
        
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']
        
        
        if not description:
            messages.error(request,'Amount is required')
            return render(request,'income/add_income.html',context)
        
        userincome.objects.create(owner=request.user,amount=amount,date=date,source=source,description=description)
        
        messages.success(request,'income saved successfully')
        
        return redirect('income')
            
    
    
    return render(request,'income/add_income.html',context)





def income_edit(request,id):
    income  =userincome.objects.get(id=id)
    sources = Source.objects.all()
    context = {
      'income':income,
      'values':income,
      'sources':sources,
    }
       
    

    if request.method=="POST":
        print("akljklasdjksad")
        amount = request.POST['amount']
        description = request.POST['description']
        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'income/edit_income.html',context)
        
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']
        
        
        if not description:
            messages.error(request,'Amount is required')
            return render(request,'income/edit_income.html',context)
        
        
        
        income.amount = amount 
        income.date = date
        income.source = source
        income.description = description
        
        
        income.save()
        messages.success(request,'Expense updated successfully')
        return redirect('income')
    return render(request,'income/edit_income.html',context)





def delete_income(request, id):
    income = userincome.objects.get(id=id)
    income.delete()
    messages.success(request, 'record removed')
    return redirect('income')