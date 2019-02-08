from django.urls import path
from .views import index

app_name = 'employees'
urlpatterns = [
    path('', index, name='index'),
]
