from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
import django_tables2 as tables
from django.views.decorators.csrf import csrf_protect

from .forms import AddReservationForm
from .models import Reservation
from .tables import ReservationsTable


# Create your views here.
@csrf_protect
def index(request):
    form = AddReservationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect("reservation:index")
    return render(request, "index.html", {"form": form})


class ReservationListView(tables.SingleTableView):
    template_name = 'reservations_admin.html'
    paginate_by = 10
    queryset = Reservation.objects.all()
    table_class = ReservationsTable



