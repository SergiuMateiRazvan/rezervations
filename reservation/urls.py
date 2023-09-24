from django.urls import path

from . import views

app_name = "reservation"
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "reservations/", views.ReservationListView.as_view(), name="reservations_list"
    ),
    path("reservations/remove/", views.delete, name="remove"),
    path("reservations/confirm/", views.confirm, name="confirm"),
]
