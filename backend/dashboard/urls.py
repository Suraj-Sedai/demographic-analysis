from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_data),
    path('analyze/', views.analyze_data),
    path('visualize/', views.visualize_data),
]
