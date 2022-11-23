from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_new/', views.create, name='create'),
    path('<int:post_id>/post_detail', views.detail, name='detail'),
]
