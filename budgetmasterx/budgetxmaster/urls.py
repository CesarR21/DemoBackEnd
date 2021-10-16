from django.urls import path 
from  . import views

urlpatterns = [
    path('budgetxmaster',views.BudgetList.as_view()),
    
]