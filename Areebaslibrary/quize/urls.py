from django.contrib import admin
from django.urls import path
from . import views
from .views import MCQSListView , ListView
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'quize'
urlpatterns = [
	path('index/', MCQSListView.as_view(), name='index'),
	path('index/<int:pk>',views.Topicdetail, name='topic-detail'),
	path('list/', ListView.as_view(), name='list'),
	path('list/<int:pk>',views.Sortinglist, name='list-detail'),
	
]