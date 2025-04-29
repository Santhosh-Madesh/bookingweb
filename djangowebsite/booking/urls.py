from . import views
from django.urls import path


app_name="booking"
urlpatterns = [
    path("",views.index,name="index"),
    path("/booking",views.booking_slot,name="booking_slot")
]