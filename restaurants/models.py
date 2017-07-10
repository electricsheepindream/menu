from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
# Create your models here.

User = settings.AUTH_USER_MODEL


class Restaurants(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    manager = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    slug = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ResHome:detail', kwargs={'mark': self.slug})


def res_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(res_pre_save, sender=Restaurants)
