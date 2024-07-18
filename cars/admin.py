from django.contrib import admin
from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand',)

admin.site.register(Car, CarAdmin)