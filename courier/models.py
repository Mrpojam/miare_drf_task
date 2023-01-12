from django.db import models

# Create your models here.
class Courier(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=160)
    last_name = models.CharField(max_length=160)
    
    def __str__ (self):
        return "%s_%s" % (self.first_name, self.last_name)

class Income(models.Model):

    CHOICES = (
        ('In', 'Income'),
        ('D', 'Decrease'),
        ('I', 'Increase')
    )

    Date = models.DateField()
    type = models.CharField(max_length=2, choices=CHOICES, default='In')
    value = models.PositiveBigIntegerField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    
    def __str__ (self):
        return "%s %s %s" % (self.courier, str(self.Date), str(self.value))

    class Meta:
        ordering = ['Date', 'courier']