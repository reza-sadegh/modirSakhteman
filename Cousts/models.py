from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length=40)

    class Meta:
        db_table = "Categories"

    def __str__(self):
        return self.category_name


class Cousts(models.Model):
    Description = models.CharField(max_length=255)
    Amount = models.IntegerField()
    payTime = models.DateField( null=True, blank=True)
    category_name = models.CharField(max_length=40)
    Recipient = models.CharField( null=True, blank=True,max_length=255)
    AccountNumber = models.CharField( null=True, blank=True,max_length=50)
    invoice = models.CharField(max_length=150)
    tel = models.CharField( null=True, blank=True,max_length=20)

    class Meta:
        db_table = "Cousts"

    def __str__(self):
        return self.Description
# Create your models here.
