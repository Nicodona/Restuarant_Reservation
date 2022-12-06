from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('food', views.food, name='food'),
    path('resto', views.resto, name='resto'),


    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]