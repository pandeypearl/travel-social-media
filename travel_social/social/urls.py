from django.urls import path

from . import views

app_name = 'social'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('create-post/', views.create_post, name='create_post'),
    path('<int:pk>/edit/', views.edit_post, name='edit_post'),
]