from django.urls import path

from .views import SignUpView, logout_view
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('logout/', views.logout_view, name='logout'), 
]