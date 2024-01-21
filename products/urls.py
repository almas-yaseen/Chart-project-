from django.urls import path 
from .import views 
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index,name='expenses'),
    path('expense_edit/<int:id>',views.expense_edit,name='expense_edit'),
    path('delete_expense/<int:id>',views.delete_expense,name='delete_expense'),
    path('add_expense',views.add_expense,name='add_expense'),
     path('search-expenses', csrf_exempt(views.search_expenses),name="search_expenses"),
   

    
]
