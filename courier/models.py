from django.db import models

# Create your models here.
class Courier(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=160)
    last_name = models.CharField(max_length=160)
    
    def __str__ (self):
        pass
class Trip(models.Model):
    Date = models.DateTimeField()
    income = models.BigIntegerField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    def __str__ (self):
        pass

    class Meta:
        ordering = ['Data', 'courier']