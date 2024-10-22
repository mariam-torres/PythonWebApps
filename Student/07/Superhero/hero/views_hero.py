from pathlib import Path
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Hero
from .views_reporter import get_reporter
    
class HeroListView(ListView):
    template_name = 'superhero/list.html'
    model = Hero
    context_object_name = 'heroes'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }

class HeroDetailView(DetailView):
    template_name = 'superhero/detail.html'
    model = Hero
    context_object_name = 'hero'

class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "superhero/add.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('hero_list')

    def form_valid(self, form):
        form.instance.reporter = get_reporter(self.request.user)
        return super().form_valid(form)
    

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "superhero/edit.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('hero_list')

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'superhero/delete.html'
    model = Hero
    success_url = reverse_lazy('hero_list')