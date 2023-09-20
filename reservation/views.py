from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import django_tables2 as tables
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .forms import AddReservationForm
from .models import Reservation
from .tables import ReservationsTable


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


@csrf_exempt
def delete(request):
    if request.method == "POST":
        data = request.POST.dict()
        reservation_id = data.get("id")
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        reservation.delete()
    return HttpResponseRedirect(reverse_lazy("reservation:reservations_list"))


@csrf_exempt
def confirm(request):
    if request.method == "POST":
        data = request.POST.dict()
        reservation_id = data.get("id")
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        reservation.confirmed = True
        reservation.save()
    return HttpResponseRedirect(reverse_lazy("reservation:reservations_list"))
