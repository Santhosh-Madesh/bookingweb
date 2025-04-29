from . import views
from django.urls import path


app_name="booking"
urlpatterns = [
    path("",views.index,name="index"),
    path("book_slot/",views.booking_slot,name="booking_slot"),
    path("<int:pk>/results/", views.BookDetailView.as_view(),name="book_review")
]