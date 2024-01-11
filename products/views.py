from django.shortcuts import render,HttpResponse
from .import views
# Create your views here.


def index(request):
    return render(request,'expenses/index.html')