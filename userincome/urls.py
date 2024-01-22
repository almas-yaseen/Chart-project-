from django.urls import path 
from .import views 
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index,name='income'),
    path('add_income',views.add_income,name='add_income'),
    path('income_edit/<int:id>',views.income_edit,name='income_edit'),
    path('delete_income/<int:id>',views.delete_income,name='delete_income'),
  
     
   

    
]
