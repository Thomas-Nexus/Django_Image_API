from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def dir_path(instance, filename):
    return 'images/{0}/'.format(filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Images(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=dir_path, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    likes = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author', null=True)

    def __str__(self):
        return self.title