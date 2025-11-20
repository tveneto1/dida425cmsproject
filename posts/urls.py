from django.urls import path
from .views import (HomePageView, upload_image, all_images_view, display, delete_image, slidedisplay, manage_users, toggle_superuser, read_dateline, fetch_json_view, weather_view)
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path("post/", views.upload_image, name="go_to_post"),
    path("allimages/", views.all_images_view, name="all_images"),
    path("delete_image/<str:pk>/", views.delete_image, name="delete_image"), 
    path("slidedisplay/", views.slidedisplay, name="slidedisplay"),
    path("slidedisplay/dateline/", views.read_dateline, name="dateline"),
    path("slidedisplay/dateline/getjson/", views.fetch_json_view, name="getjson"),
    path("slidedisplay/weatherview/", views.weather_view, name="weather_view"),
    path("manage-users/", views.manage_users, name="manage_users"),
    path("toggle-superuser/<str:pk>/", views.toggle_superuser, name="toggle_superuser"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
