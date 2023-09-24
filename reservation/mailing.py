from django.conf import settings
from django.core.mail import mail_admins, send_mail


def mail_customer(reservation, confirmed=True):
    if confirmed:
        subject = "Your Reservation at Ballermo confirmed"
        message = "Salut"
    else:
        subject = "Your Reservation at Ballermo NOT confirmed"
        message = ""

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
        <div>
            New reservation at {reservation.date} by {reservation.customer_name}.
            Please see the reservations page to confirm to customer.
        </div>
        <a href='{settings.RESERVATIONS_PAGE}'>See new reservation</a>
        </body>
        </html>
        
        """,
    )
