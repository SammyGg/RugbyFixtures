from django.urls import path
from . import views

urlspatterns = [
    path ('<int:id>', views.detail, name="details"),
    path ('clubs', views.club_list, name="clubs"),
]