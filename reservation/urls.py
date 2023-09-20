from django.urls import path

from . import views

appname = 'reservation'
urlpatterns = [
    path('', views.index, name='index')
]
