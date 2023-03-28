from rest_framework import viewsets
from .serializers import ProductSerializer,CategorySerializer
from . models import Product,Category
from django.db.models import Sum, Max, Min, Avg
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filterset_fields=['product_name','amount','date_added','category']
    filter_backends=[OrderingFilter]
    # ordering_fields=['date_added']
    # authentication_classes=[BasicAuthentication]
    authentication_classes=[SessionAuthentication]

    permission_classes=[IsAuthenticated]
    

  
    


    # def example(request):
    #     sum=Product.objects.aggregate(sum=Sum('amount'))
    #     max=Product.objects.aggregate(max=Max('amount'))
    #     min=Product.objects.aggregate(min=Min('amount'))
    #     avg=Product.objects.aggregate(avg=Avg('amount'))

    #     return(request)
@api_view(['GET'])
def example(request):
    data = Product.objects.aggregate(sum=Sum('amount'), max=Max('amount'),min=Min('amount'),avg=Avg('amount'))
    return Response({"data":data})

# @api_view(['GET'])
# def examples(request):
#     datas = Product.objects.annotate(avg=Avg('amount'))
#     return Response({"data":datas})



class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    filterset_fields=['category']
    


