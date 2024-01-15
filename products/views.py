from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .import views
from django.views.decorators.cache import never_cache

# Create your views here.

@login_required(login_url='/authentication/login')
@never_cache
def index(request):
    return render(request,'expenses/index.html')


def add_expense(request):
    return render(request,'expenses/add_expense.html')