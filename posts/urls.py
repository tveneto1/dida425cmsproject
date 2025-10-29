from django.urls import path

from .views import HomePageView, upload_image, all_images_view, display, delete_image

from . import views

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path("post/", views.upload_image, name="go_to_post"),
    path("allimages/", views.all_images_view, name="all_images"),
    path("delete_image/<str:pk>/", views.delete_image, name="delete_image"), #got this from tutorial, does not work :(
    path("displaypath/", views.display, name="slidedisplay"),
]