from django.urls import path
from .views import IndexView, GalleryView, admin_upload
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("admin-upload/", admin_upload, name="admin-upload"),

]