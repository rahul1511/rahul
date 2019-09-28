from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=50)
    eid=models.IntegerField(max_length=10)
    email=models.EmailField(max_length=50)
    salery=models.DecimalField(max_digits=20 , decimal_places=2)
    def __str__(self):
        return self.name
