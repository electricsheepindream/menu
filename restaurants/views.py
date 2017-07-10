from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Restaurants
from .forms import ResForm
from django.contrib.auth.views import PasswordResetView
# Create your views here.


class ResLisView(ListView):
    queryset = Restaurants.objects.all()
    template_name = 'home.html'


class WestResLisView(ListView):
    queryset = Restaurants.objects.all().filter(type__iexact='west')
    template_name = 'home.html'


class EastResLisView(ListView):
    queryset = Restaurants.objects.all().filter(type__iexact='east')
    template_name = 'home.html'


class SearchListView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = Restaurants.objects.all().filter(type__iexact=slug)
        return queryset


class ResDetailView(DetailView):
    template_name = 'detail.html'
    model = Restaurants

    def get_context_data(self, **kwargs):
        context = super(ResDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self, *args, **kwargs):
        mark = self.kwargs.get('mark')
        obj = get_object_or_404(Restaurants, slug=mark)
        return obj


class ResCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = ResForm
    template_name = 'res_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ResCreateView, self).form_valid(form)


class PasswordReset(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'email.html'
    subject_template_name = 'password_reset.txt'
    success_url = '/restaurants/listview/'
    from_email = 'electricsheepindream@gmail.com'










