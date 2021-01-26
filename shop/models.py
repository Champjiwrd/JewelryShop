from django.db import models

# Create your models here.

class Jewelry(models.Model):
    jewelry_name = models.CharField(max_length = 200,blank=True , null=True)
    jewelry_photo = models.ImageField(upload_to="jewelryphoto",blank=True,null=True)
    jewelry_about = models.TextField(blank=True, null=True)
    jewelry_price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return '{}'.format(self.jewelry_name)