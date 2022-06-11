from django.contrib import admin
from cars.models import Car
# Register your models here.

#this allows to customize the Admin page
class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TIME INFORMATION', {'fields':['year']}),
        ('CAR INFORMATION',{'fields':['brand']})
    ]

admin.site.register(Car, CarAdmin)