from rest_framework import viewsets
from .serializers import ProductSerializer,CategorySerializer
from . models import Product,Category
from django.db.models import Sum, Max, Min, Avg
from django.shortcuts import render

# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filterset_fields=['product_name']
    filterset_fields=['amount']
    filterset_fields=['date_added']
    filterset_fields=['category']


    # def example(request):
    #     sum=Product.objects.aggregate(sum=Sum('amount'))
    #     max=Product.objects.aggregate(max=Max('amount'))
    #     min=Product.objects.aggregate(min=Min('amount'))
    #     avg=Product.objects.aggregate(avg=Avg('amount'))

    #     return(request)

# def example(request):
#   data = Product.objects.aggregate(sum=Sum('amount'), max=Max('amount'),min=Min('amount'),avg=Avg('amount'))
#   return (request,{"data":data})
data = Product.objects.aggregate(sum=Sum('amount'), max=Max('amount'),min=Min('amount'),avg=Avg('amount'))
print(data)

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    filterset_fields=['category']

