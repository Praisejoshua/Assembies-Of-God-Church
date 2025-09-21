from django.db import models

class Post(models.Model):
    topic = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # timestamp for the post

    def __str__(self):
        return self.topic


class GalleryImage(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery/")  # save images in MEDIA_ROOT/gallery/

    def __str__(self):
        return f"Image for {self.post.topic}"
