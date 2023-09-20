from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddReservationForm


# Create your views here.
def index(request):
    form = AddReservationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect("reservation:index")
    return render(request, "index.html", {"form": form})
