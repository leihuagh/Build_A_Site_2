from django.urls import path
from .views import index

app_name = 'polls'
urlpatterns = [
    path('', index, name='index'),
]
