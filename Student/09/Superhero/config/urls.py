from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from hero.views_hero import HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView
from hero.views_reporter import ReporterHomeView, ReporterAddView, ReporterDetailView, ReporterListView, ReporterUpdateView
from django.contrib.auth.views import LogoutView  
urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',  RedirectView.as_view(url='/reporter/home')),
    
    path('logout/', LogoutView.as_view(next_page='hero_list'), name='logout'),

    path('',                     RedirectView.as_view(url='hero/')),
    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    path('reporter/',                    ReporterListView.as_view(),    name='reporter_list'),
    path('reporter/home',                ReporterHomeView.as_view(),    name='reporter_home'),
    path('reporter/<int:pk>',            ReporterDetailView.as_view(),  name='reporter_detail'),
    path('reporter/add/',                ReporterAddView.as_view(),     name='reporter_add'),
    path('reporter/<int:pk>/',           ReporterUpdateView.as_view(),  name='reporter_edit'),
    path('reporter/<int:pk>/edit/',      ReporterUpdateView.as_view(), name='reporter_update'),
]