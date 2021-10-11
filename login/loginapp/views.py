from .models import Login
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  serializers, status

# Create your views here.
class LoginList(APIView):

    def get(self, request):
        login = Login.objects.all()
        serializer = LoginSerializer(login, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)