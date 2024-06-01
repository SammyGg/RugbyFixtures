from django.shortcuts import render, get_object_or_404
from .models import Fixture, Club
def detail(request, id):
    fixture = get_object_or_404(Fixture, pk=id)
    return render(request, "fixtures/detail.html",{"fixture": fixture})
def club_list(request):
    return render(request, "fixtures/clubs_list.html",
                     {"clubs": Club.objects.all()})