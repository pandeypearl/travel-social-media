from django.urls import path

from . import views
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
]