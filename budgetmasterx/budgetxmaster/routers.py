from rest_framework import routers
from .viewsets import BudgetViewSet
router = routers.SimpleRouter()
router.register(r'budget', BudgetViewSet, basename='budget')


#restaurant/urls.py
from django.contrib import admin
from django.urls import path, include
from routers import router

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'budgetmasterx'), namespace='budgetmasterx'))
]