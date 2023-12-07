# from U_Auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)
    Status = models.IntegerField(default=1)
    Reference = models.CharField(max_length=25)
    Added_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(default=1)

    Added_Date = models.DateTimeField(auto_now_add=True)

    Reference = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    seo_url = models.CharField(max_length=200)
    seo_title = models.CharField(max_length=200)
    seo_description = models.TextField()
    seo_keywords = models.CharField(max_length=200)

    Added_Date = models.DateTimeField(auto_now_add=True)

    Reference = models.CharField(max_length=25)

    Status = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
