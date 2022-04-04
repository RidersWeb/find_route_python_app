from django.contrib import admin

from cities.models import City
from cities.models import Street

class CityAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(City, CityAdmin)
admin.site.register(Street)
