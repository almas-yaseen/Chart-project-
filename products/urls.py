from django.urls import path 
from .import views 

urlpatterns = [
    path('',views.index,name='expenses'),
     path('expense_edit/<int:id>',views.expense_edit,name='expense_edit'),
    path('add_expense',views.add_expense,name='add_expense'),
   

    
]
