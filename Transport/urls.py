from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^TransportVehicle/$', TransportVehicle, name='TransportVehicle'),
    re_path(r'^TransportDriver/$', TransportDriver, name='TransportDriver'),
    re_path(r'^TransportConductor/$', TransportConductor, name='TransportConductor'),
    re_path(r'^TransportVehicleExpenses/$', TransportVehicleExpenses, name='TransportVehicleExpenses'),
    re_path(r'^TransportAssignStudent/$', TransportAssignStudent, name='TransportAssignStudent'),
    re_path(r'^TransportAddFees/$', TransportAddFees, name='TransportAddFees'),
    re_path(r'^TransportFeesDetail/$', TransportFeesDetail, name='TransportFeesDetail'),
]