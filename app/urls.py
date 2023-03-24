
from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('product', views.ProductModelViewSet)
router.register('category',views.CategoryModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('home/',views.example),
]
