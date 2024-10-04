from django.urls import path
from . import views


urlpatterns = [
  path('userManagement/',views.userManagement, name='userManagement'),
  path('create_user/', views.createUser, name='createUser'),
  path('homepage/', views.home_page, name='home_page'),
  path('files/', views.files, name='files'),
  path('archive/', views.archive, name='archive'),
  path('myprofile/', views.my_profile, name='my_profile'),

]