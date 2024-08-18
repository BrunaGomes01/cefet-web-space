from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('philae', views.Philae.as_view(), name='philae'),
]