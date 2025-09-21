from django import forms
from .models import GalleryImage

class GalleryUploadForm(forms.Form):
    topic = forms.CharField(max_length=255)
    image = forms.ImageField()  # single, but we'll grab multiple in the view

