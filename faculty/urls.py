from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('submission/', views.submission_bin_page, name='submission_bin_page'),
    path('my_portfolio/', views.my_portfolio_page, name='my_portfolio_page'),
    path('my_profile/', views.profile_page, name='profile_page'),
]