from django.db import models

class Productdb(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

class Meta:
    db_table = "Productdb"
