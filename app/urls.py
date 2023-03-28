
from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('product', views.ProductModelViewSet)
router.register('category',views.CategoryModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('aggregate/',views.example),
    # path('annotate/',views.examples),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))#SESSION AUTHENTICATION

]
