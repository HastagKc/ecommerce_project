from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('about/',about_us,name='about'),
    path('product/',product,name='product'),
    path('sign_up/',sign_up,name='sign_up'),
]
