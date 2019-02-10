from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('employees/', include('employees.urls')),
    path('polls/', include('polls.urls')),
]
