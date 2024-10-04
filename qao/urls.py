from django.urls import path
from . import views


urlpatterns = [
  path('homePage/',views.homePage, name='homePage'),
  path('filespage/',views.filespage, name='filespage'),
  path('myprofile/',views.myprofile, name='myprofile')
]