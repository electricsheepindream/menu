from django.db import models
from django.conf import settings
from restaurants.models import Restaurants
from django.core.urlresolvers import reverse


class Menu(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurants = models.ForeignKey(Restaurants)
    menu_name = models.CharField(max_length=120)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_name

    class Meta:
        ordering = ('edit_time', 'create_time')
    # def get_absolute_url(self):
    #     return reverse('ResHome:detail', kwargs={'mark': self.slug})


class Items(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=120)
    item_price = models.IntegerField(default=0)
    item_number = models.IntegerField(default=0)
    item_popular = models.IntegerField(default=0)
    item_description = models.TextField(null=True, blank=True)
    item_img = models.ImageField()

    def __str__(self):
        return self.item_name

    # def get_absolute_url(self):
    #     return reverse('ResHome:detail', kwargs={'mark': self.slug})