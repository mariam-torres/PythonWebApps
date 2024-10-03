from django.contrib import admin
from django.urls import path
from hero.views import HeroDetailView, HeroListView

urlpatterns = [
    path("", HeroListView.as_view()),
    path("hero/<str:numID>", HeroDetailView.as_view())
]
