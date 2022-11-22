from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/', views.create, name='create'),
]