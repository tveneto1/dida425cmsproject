from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uploads/', views.upload_list, name='uploads'),
    path('upload/', views.upload_image, name='upload_image')
]