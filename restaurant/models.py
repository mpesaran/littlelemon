from django.db import models

# Create your models here.
class Menu(models.Model):
    ID = models.IntegerField(primary_key=True, db_index=True)
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits = 10 , decimal_places=2)
    Inventory = models.SmallIntegerField()

class Booking(models.Model):
    ID = models.IntegerField(primary_key=True,db_index=True)
    Name = models.CharField(max_length =255)
    No_of_guests = models.SmallIntegerField()
    BookingDate = models.DateField(db_index=True)