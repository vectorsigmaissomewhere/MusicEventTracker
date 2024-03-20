from django.db import models

# Create your models here.
class MusicalEvent(models.Model):
    artist = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    time = models.DateTimeField()
    district = models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.artist + ' - ' + self.place + ' - ' + str(self.time)
