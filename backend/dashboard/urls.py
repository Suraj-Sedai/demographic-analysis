from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_data, name='generate_data'),
    path('analyze/', views.analyze_data, name='analyze_data'),
]
