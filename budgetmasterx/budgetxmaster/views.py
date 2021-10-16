from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Budget
from .serializers import BudgetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.all()

class BudgetList(APIView):
    def get(self,request):
        budget = Budget.objects.all()
        serializer = BudgetSerializer(budget,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BudgetDetail(APIView):
    def get_object(self,pk):
        try:
            return Budget.objects.get(pk=pk)
        except Budget.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(slef,request,pk):
        budget = slef.get_object(pk)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)
    def put(self,request,pk):
        budget = self.get_object(pk)
        serializer = BudgetSerializer(budget,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializers.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        budget = self.get_object(pk)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)