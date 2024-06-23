from django.urls import path
from . import views
#from rfixtures.views import detail, club_list

urlpatterns = [
    path ('<int:id>', views.detail, name="detail"),
    path ('clubs', views.club_list, name="clubs"),
    path('new', views.new, name="new")
]