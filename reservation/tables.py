import itertools

import django_tables2 as tables
from django.urls import reverse_lazy
from django.utils.html import format_html

from .models import Reservation


class ReservationsTable(tables.Table):
    customer_name = tables.Column(
        attrs={"th": {"scope": "col"}}, footer=lambda table: f"Total: {len(table.data)}"
    )
    customer_email = tables.Column(attrs={"th": {"scope": "col"}})
    customer_phone = tables.Column(attrs={"th": {"scope": "col"}})
    no_persons = tables.Column(attrs={"th": {"scope": "col"}})
    date = tables.Column(attrs={"th": {"scope": "col"}})
    time = tables.Column(attrs={"th": {"scope": "col"}})
    mentions = tables.Column(attrs={"th": {"scope": "col"}})
    confirmed = tables.Column(attrs={"th": {"scope": "col"}})
    delete = tables.Column(verbose_name="", empty_values=())

    class Meta:
        model = Reservation
        attrs = {"class": "table"}
        fields = (
            "customer_name",
            "customer_email",
            "customer_phone",
            "no_persons",
            "date",
            "time",
            "mentions",
        )
        sequence = (
            "customer_name",
            "customer_email",
            "customer_phone",
            "no_persons",
            "date",
            "time",
            "mentions",
            "confirmed",
            "delete",
        )

    def render_confirmed(self, value, record):
        if value:
            return "Confirmed"
        else:
            return format_html(
                '<form method="POST" action="{}">\
                    <input type="hidden" name="id" value="{}">\
                    <button type="submit" class="btn btn-primary">Confirm</button>\
                </form>',
                reverse_lazy("reservation:confirm"),
                record.id,
            )

    def render_delete(self, value, record):
        return format_html(
            '<form method="POST" action="{}"> \
                <input type="hidden" name="id" value="{}">\
                <button type="submit" class="btn btn-danger">Delete</button>\
            </form>',
            reverse_lazy("reservation:remove"),
            record.id,
        )


class ExpiredReservationsTable(ReservationsTable):
    delete = None

    class Meta:
        model = Reservation
        attrs = {"class": "table table-secondary text-muted"}
        fields = (
            "customer_name",
            "customer_email",
            "customer_phone",
            "no_persons",
            "date",
            "time",
            "mentions",
        )
        sequence = (
            "no",
            "customer_name",
            "customer_email",
            "customer_phone" "no_persons",
            "date",
            "time",
            "mentions",
            "confirmed",
        )

    def render_confirmed(self, value, record):
        return "Confirmed" if value else "Not confirmed"
