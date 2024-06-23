from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Fixture, Club
from .form import FixtureForm
def detail(request, id):
    fixture = get_object_or_404(Fixture, pk=id)
    return render(request, "fixtures/detail.html",{"fixture": fixture})

def club_list(request):
    return render(request, "fixtures/clubs_list.html",
                     {"clubs": Club.objects.all()})
# fixtureForm= modelform_factory(Fixture, exclude=[])

def new(request):
    if request.method=="POST":
       form= FixtureForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("welcome")
    else:
        form=FixtureForm()
    return render(request, "fixtures/new.html",{"form": form})