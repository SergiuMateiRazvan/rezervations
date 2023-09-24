from django.core.mail import send_mail, mail_admins
from django.conf import settings


def mail_customer(reservation):
    subject = "Your Reservation at Ballermo confirmed"
    message = "Salut"

    success = send_mail(
        subject, message, settings.EMAIL_ADDR, [reservation.customer_email]
    )

    if not success:
        raise Exception("Error sending message")


def mail_admin(reservation):
    mail_admins(
        "New reservation",
        message="",
        html_message=f"""
        <html>
        <body>
        <button><a href='{settings.RESERVATIONS_PAGE}'>See new reservation</a></button>
        </body>
        </html>
        
        """
    )
