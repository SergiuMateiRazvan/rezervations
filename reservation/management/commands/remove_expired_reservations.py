from datetime import datetime

from django.core.management.base import BaseCommand
from reservation.models import Reservation


class RemoveExpiredReservationsCommand(BaseCommand):
    def handle(self, *args, **options):
        for reservation in Reservation.objects.iterator():
            if reservation.date < datetime.today():
                reservation.delete()
