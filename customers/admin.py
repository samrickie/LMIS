from django.contrib import admin
from .models import BankAccount, Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'middle_name', 'age']

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(BankAccount)