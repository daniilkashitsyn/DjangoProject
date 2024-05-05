from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('quality_control/', include('quality_control.urls')),
    path('', include('tasks.urls')),
]