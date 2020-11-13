from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .utils import unique_slug_generator
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" %(instance.title, instance.title, extension)
    BlogPostModel = instance.__class__
    new_id = BlogPostModel.objects.order_by("instance.title").last().id + 1

    return "%s" %(filename)






class BlogPost(models.Model):
    user         = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    title        = models.CharField(max_length=120)
    slug         = models.SlugField(unique=True, null=True, blank=True)
    image        = models.ImageField(upload_to=upload_location, null=True, blank=True)
    content      = models.TextField(null=True, blank=True)
    draft        = models.BooleanField(default=False)
    publish      = models.DateField(auto_now=False, auto_now_add=False)
    updated      = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp    = models.DateTimeField(auto_now=False, auto_now_add=True)



    def __str__(self):
        return str(self.title)






def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Job.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug




def pre_save_job_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_job_receiver, sender=BlogPost)

