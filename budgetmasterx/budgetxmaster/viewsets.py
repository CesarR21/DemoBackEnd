from rest_framework import serializers, viewsets
from .models import Budget
from .serializers import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    serializers_class = BudgetSerializer