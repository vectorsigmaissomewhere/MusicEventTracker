from django.db import models

#now we need user interaction as foreign key while sending feedback to admin
from django.contrib.auth.models import User

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
    

class OurProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_size = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.product_name
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback from {self.user.username if self.user else "Anonyous"}'
