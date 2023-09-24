import logging
from datetime import date

from django.core.management.base import BaseCommand

from reservation.models import Reservation

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("Started removing expired reservations")
        removal_counter = 0
        for reservation in Reservation.objects.iterator():
            if reservation.date < date.today():
                logger.info(
                    f"Removing reservation for {reservation.id}-{reservation.customer_name}"
                )
                reservation.delete()
                removal_counter += 1
        logger.info(f"Finished removing {removal_counter} reservations")
