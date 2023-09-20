import itertools

import django_tables2 as tables
from django.urls import reverse_lazy
from django.utils.html import format_html
from .models import Reservation


class ReservationsTable(tables.Table):
    customer_name = tables.Column(attrs={
        "th": {"scope": "col"}
    })
    customer_email = tables.Column(attrs={
        "th": {"scope": "col"}
    })
    no_persons = tables.Column(attrs={
        "th": {"scope": "col"}
    })
    date = tables.Column(attrs={
        "th": {"scope": "col"}
    })
    time = tables.Column(attrs={
        "th": {"scope": "col"}
    })
    mentions = tables.Column(attrs={
        "th": {"scope": "col"}
    })
    confirmed = tables.Column(attrs={
        "th": {"scope": "col"}
    })
    delete = tables.Column(verbose_name="", empty_values=(), accessor="id")

    class Meta:
        model = Reservation
        attrs = {"class": "table"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_confirmed(self, value):
        if value:
            return "Confirmed"
        else:
            return format_html(
                '<form method="POST" action="">\
                    <input type="hidden" name="id" value="{}">\
                    <button type="submit" class="btn btn-primary">Confirm</button>\
                </form>', 1
            )

    def render_delete(self, value):
        return format_html(
            '<form method="POST" action="{}"> \
                <input type="hidden" name="id" value="{}">\
                <button type="submit" class="btn btn-danger">Delete</button>\
            </form>', reverse_lazy("reservation:remove"), value
        )
