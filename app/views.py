from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .forms import GalleryUploadForm
from .models import GalleryImage, Post


# Create your views here.

class IndexView(TemplateView):
    template_name = 'html/index.html'

class GalleryView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'html/gallery.html'
    ordering = ['-uploaded_at']

class AdminView(TemplateView):
    template_name = 'html/admin.html'


from django.shortcuts import render, redirect
from .models import Post, GalleryImage

# Gallery upload function
def admin_upload(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        images = request.FILES.getlist("image")

        # Create a new post
        post = Post.objects.create(topic=topic)

        # Attach all uploaded images to this post
        for img in images:
            GalleryImage.objects.create(post=post, image=img)

        return redirect("gallery")

    return render(request, "html/admin.html")


# Gallery display
def gallery(request):
    # Get all posts with related images, newest first
    posts = Post.objects.prefetch_related("images").order_by("-uploaded_at")
    return render(request, "html/gallery.html", {"posts": posts})



