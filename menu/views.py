from django.shortcuts import render, get_object_or_404
from .models import Menu, Items
from restaurants.models import Restaurants
from django.views.generic import ListView, DetailView, DeleteView, UpdateView


class MenuListView(ListView):
    template_name = 'menu/menu_list.html'
    obj = Menu.restaurants
    queryset = obj.menu_set.all()
