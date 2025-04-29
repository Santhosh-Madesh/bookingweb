from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class AvSlots(models.Model):
    available_slots = models.IntegerField(validators=[MaxValueValidator(24),MinValueValidator(0)])
    date = models.DateField()

    def __str__(self):
        slots_remaining = str(self.available_slots)
        return slots_remaining


class Book(models.Model):
    avslots = models.ForeignKey(AvSlots, on_delete=models.CASCADE)
    date = models.DateField()
    slot_num = models.IntegerField()

    def __str__(self):
        value = "slot "+str(self.slot_num)
        return value
