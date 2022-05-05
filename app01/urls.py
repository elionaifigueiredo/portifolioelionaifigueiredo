from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/projetos', views.projetos, name="projetos"),
    path('/parceiros', views.parceiros, name="parceiros"),
]