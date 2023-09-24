from datetime import datetime

import django_tables2 as tables
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .forms import AddReservationForm
from .mailing import mail_admin, mail_customer
from .models import Reservation
from .tables import ExpiredReservationsTable, ReservationsTable


def index(request):
    form = AddReservationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            mail_admin(reservation)
            return redirect("reservation:index")
    return render(request, "index.html", {"form": form})


class ReservationListView(LoginRequiredMixin, tables.MultiTableMixin, TemplateView):
    template_name = "reservations_admin.html"
    paginate_by = 10
    queryset = Reservation.objects.filter(date__gte=datetime.today()).all()
    queryset_2 = Reservation.objects.filter(date__lt=datetime.today()).all()
    tables = (
        [ReservationsTable(queryset), ExpiredReservationsTable(queryset_2)]
        if len(queryset_2)
        else [ReservationsTable(queryset)]
    )


@csrf_exempt
def delete(request):
    if request.method == "POST":
        data = request.POST.dict()
        reservation_id = data.get("id")
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        mail_customer(reservation, confirmed=False)
        reservation.delete()
    return HttpResponseRedirect(reverse_lazy("reservation:reservations_list"))


@csrf_exempt
def confirm(request):
    if request.method == "POST":
        data = request.POST.dict()
        reservation_id = data.get("id")
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        mail_customer(reservation)
        reservation.confirmed = True
        reservation.save()
    return HttpResponseRedirect(reverse_lazy("reservation:reservations_list"))
