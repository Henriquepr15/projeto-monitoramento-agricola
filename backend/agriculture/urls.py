from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.get_climate_data, name='get_climate_data'),
    path('area/', views.calculate_area, name='calculate_area'),
    path('simulation/', views.simulate_crop, name='simulate_crop'),
]
