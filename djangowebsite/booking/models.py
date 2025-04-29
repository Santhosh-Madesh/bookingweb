from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.BigIntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    slot_num = models.IntegerField()

    def __str__(self):
        value = "slot "+str(self.slot_num)
        return value
