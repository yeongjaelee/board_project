from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_new/', views.create, name='create'),
    path('<int:post_id>/post_detail', views.detail, name='detail'),
    path('<int:delete_post_id>/post_list', views.index, name="delete"),
    path('<int:post_id>/post_detail', views.update, name='update'),
]
