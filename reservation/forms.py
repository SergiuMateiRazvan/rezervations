import datetime
from django import forms
from .models import Reservation
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput


class AddReservationForm(forms.ModelForm):
    mentions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Reservation
        fields = ('date', 'time', 'no_persons', 'customer_name', 'customer_email', 'mentions')

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date': DatePickerInput(
                attrs={'class': 'form-control'},
                options={
                    'locale': 'it',
                    'format': 'DD/MM/YYYY',
                    'showTodayButton': True,
                    'maxDate': datetime.date.today() + datetime.timedelta(days=14),
                    'minDate': datetime.date.today(),
                    # 'todayHighlight': True
                    # 'today': "Today",
                }
            ),
            'time': TimePickerInput(
                attrs={'class': 'form-control'},
                options={
                    'locale': 'it',
                    'format': 'HH:mm',
                    'stepping': 30,
                    'minDate': (datetime.datetime.today() - datetime.timedelta(hours=datetime.datetime.today().hour,
                                                                               minutes=datetime.datetime.today().minute) + datetime.timedelta(
                        hours=19)).hour,
                    'maxDate': datetime.date.today() + datetime.timedelta(hours=23)
                }
            ),
            'no_persons': forms.NumberInput(attrs={'class': 'form-control'}),

        }
