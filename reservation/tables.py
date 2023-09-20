import itertools

import django_tables2 as tables
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
                "<button class='btn btn-outline-primary'> Confirm </button>"
            )
