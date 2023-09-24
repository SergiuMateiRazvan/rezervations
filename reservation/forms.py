import datetime

from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django import forms

from .models import Reservation


class AddReservationForm(forms.ModelForm):
    mentions = forms.CharField(
        widget=forms.Textarea(attrs={"class": "box-b"}), required=False
    )

    class Meta:
        model = Reservation
        fields = (
            "date",
            "time",
            "no_persons",
            "customer_name",
            "customer_email",
            "customer_phone",
            "mentions",
        )

        widgets = {
            "customer_name": forms.TextInput(
                attrs={"class": "box-b", "placeholder": "Scrivi il tuo nome e cognome"}
            ),
            "customer_email": forms.EmailInput(
                attrs={"class": "box-b", "placeholder": "Scrivi il tuo indirizzo email"}
            ),
            "customer_phone": forms.NumberInput(
                attrs={
                    "class": "box-b",
                    "placeholder": "Scrivi il tuo numero di telefono",
                }
            ),
            "date": DatePickerInput(
                attrs={"class": "box-b"},
                options={
                    "locale": "it",
                    "format": "DD/MM/YYYY",
                    "showTodayButton": True,
                    "maxDate": datetime.date.today() + datetime.timedelta(days=14),
                    "minDate": datetime.date.today(),
                },
            ),
            "time": forms.Select(
                choices=(
                    ("19:00", "19:00"),
                    ("19:30", "19:30"),
                    ("20:00", "20:00"),
                    ("20:30", "20:30"),
                    ("21:00", "21:00"),
                    ("21:30", "21:30"),
                ),
                attrs={"class": "box-b", "placeholder": "Seleziona l'orario"},
            ),
            # "time": TimePickerInput(
            #     attrs={"class": "box-b"},
            #     options={
            #         "locale": "it",
            #         "format": "HH:mm",
            #         "stepping": 30,
            #         "minDate": (
            #             datetime.datetime.today()
            #             - datetime.timedelta(
            #                 hours=datetime.datetime.today().hour,
            #                 minutes=datetime.datetime.today().minute,
            #             )
            #             + datetime.timedelta(hours=19)
            #         ).hour,
            #         "maxDate": datetime.date.today() + datetime.timedelta(hours=23),
            #     },
            # ),
            "no_persons": forms.NumberInput(attrs={"class": "box-b"}),
        }
