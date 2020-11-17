from django.urls import path
from . import views
urlpatterns = [
path('',views.HomePageView, name='home'),
path('edit/',views.edit, name='edit'),
]
