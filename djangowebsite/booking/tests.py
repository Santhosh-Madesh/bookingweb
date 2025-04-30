from django.test import TestCase
from .models import Slot
import datetime

class SlotModelTest(TestCase):
    def test_if_date_hour_repeats(self):
        book1 = Slot(date=datetime.date.today(),hour=5,is_booked=True)
        book2 = Slot(date=datetime.date.today(),hour=5,is_booked=True)

        flag = True

        if book1.date == book2.date and book1.hour == book2.hour:
            flag = False

            
        self.assertIs(flag,True)
    
    def test_if_date_is_in_the_past(self):
        book1 = Slot(date=datetime.date(2025,4,29),hour=4,is_booked=True)

        flag = True

        if book1.date<datetime.date.today():
            flag = False

        self.assertIs(flag,True)

