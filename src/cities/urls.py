from django.urls import path, re_path

from cities.views import *

from cities.views import CityUpdateView

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    re_path(r'^page/(?P<page_num>[0-9]{1})', page)
]
