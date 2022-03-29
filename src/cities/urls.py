from django.urls import path

from cities.views import *

from find_route.src.cities.views import CityUpdateView

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete')
]