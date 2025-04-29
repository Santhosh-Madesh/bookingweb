from django.db import models

class Slot(models.Model):
    date = models.DateField()
    hour = models.PositiveSmallIntegerField(choices=[(i,f"{i}:00") for i in range(24)])
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('date','hour')

    def __str__(self):
        return f"{self.date}-{self.hour}:00"