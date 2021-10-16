from rest_framework import fields, serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id','balance','Income','expense','date','category','amount','spent']
