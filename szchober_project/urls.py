from django.contrib import admin
from django.urls import path, include
from szchober import views

'''
----------------------------------------------------------------------------------------------------------------
 urls.py file - registers the web apps urls. maps urls for:
    - index
    - about us
    - feedback

Heather 2375346c, finished 31/03/20
----------------------------------------------------------------------------------------------------------------
'''

urlpatterns = [
    path('', views.index, name='szchober'),
    path('about-us/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('szchober/', include('szchober.urls')),
    path('admin/', admin.site.urls),
]
