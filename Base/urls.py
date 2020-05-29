from django.urls import path
from .views import * 
urlpatterns = [
    path('', home, name = 'homepage'),
	path('next/', home2, name = 'homepage2'),
	
]