from django.urls import path
from . import views

app_name = 'dds_app'

urlpatterns = [
    path('get_categories/', views.get_categories, name='get_categories'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
]