from django.urls import path

from .views import HomePageView, CreatePostView

from . import views

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path("post/", views.upload_image, name="upload_image"),
]