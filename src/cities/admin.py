from django.contrib import admin

from cities.models import City
from cities.models import Street

admin.site.register(City)
admin.site.register(Street)
