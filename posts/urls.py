from django.urls import path

from .views import HomePageView, CreatePostView, upload_image, all_images_view, display

from . import views

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path("post/", views.upload_image, name="go_to_post"),
    path("allimages/", views.all_images_view, name="all_images"),
    path("displaypath/", views.display, name="slidedisplay")
]