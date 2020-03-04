from django.contrib import admin
from django.urls import path, include
from szchober import views

urlpatterns = [
    path('', views.index, name='szchober'),
    path('szchober/', include('szchober.urls')),
    path('admin/', admin.site.urls),
]
