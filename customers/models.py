
from datetime import datetime
from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField()
    customer_type = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    # returns-a-human-readable-string
    def __str__(self):
        # f is used to set the placeholder
        return f'{self.first_name} {self.last_name}'

    def get_year_of_birth(self):
        year = datetime.datetime.today().year
        yob = int(year) - int(self.age)
        return yob


class BankAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    account_number = models.CharField(max_length=13)
    balance = models.IntegerField()

    def __str__(self):
        return self.account_number
