from django.shortcuts import render
from rest_framework.response import Response # 1
from rest_framework.decorators import api_view # 2
from .models import Category
from .serializer import CategorySerializer

# Create your views here.
@api_view(["GET"])
def hello_world(request):
    return Response({"message" : "Hello World"})

@api_view(["GET"])
def categories(request) :
    queryset = Category.objects.all()
    serialized = CategorySerializer(queryset, many=True) # 1
    return Response(serialized.data)