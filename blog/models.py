from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(null=True, blank=True, max_length=200)  
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="placeholder.png")
    body     = RichTextUploadingField(null=True, blank=True)
    created  = models.DateTimeField(editable=False)
    modified = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags     = models.ManyToManyField(Tag, null=True, blank=True)
    slug     = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        # Only for object create
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()

        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            i = 1
            while has_slug:
                i += 1
                slug = slugify(self.headline) + '-' + str(i)
                has_slug = Post.objects.filter(slug=slug).exists()
            self.slug = slug

        return super().save(*args, **kwargs)