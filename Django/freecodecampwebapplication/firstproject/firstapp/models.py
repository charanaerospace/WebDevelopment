from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Reservations(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    guest_count= models.IntegerField()
    resevation_time= models.DateTimeField(auto_now=True)
    Comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name
