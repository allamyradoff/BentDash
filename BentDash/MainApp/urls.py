from django.urls import path
from MainApp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('category/<str:slug>/', category, name='category'),
    path('product_all/', product_all, name='product_all'),
    path('product_single/<str:slug>/<int:id>/', product_single, name='single-product'),
    path('product/<str:slug>/', product, name='product'),
    path('about/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
]
