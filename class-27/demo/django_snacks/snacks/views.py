from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class SnacksPageView(ListView):
    template_name = 'snacks.html'
    model = Snack


class SnackDetailPageView(DetailView):
    template_name = 'snacks_detail.html'
    model = Snack
