from django.urls import path

from .views import HomePageView, CreatePostView, upload_image, all_images_view

from . import views

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path("post/", views.upload_image, name="go_to_post"),
    path("all_images/", views.all_images_view, name="uploaded_images")
]