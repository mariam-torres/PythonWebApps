from django.urls import path
from hero.views import IndexView, SpidermanView, StormView, WandaView, X23View


urlpatterns = [
    path('',            IndexView.as_view()),
    path('hero/spiderman',        SpidermanView.as_view()),
    path('hero/storm',        StormView.as_view()),
    path('hero/wanda',  WandaView.as_view()),
    path('hero/x23',  X23View.as_view()),
]
