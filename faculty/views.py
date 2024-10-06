from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def homepage(request):
  return render(request,'faculty/homepage.html')


def submission_bin_page(request):
  return render(request,'faculty/submission_bin_page.html')


def my_portfolio_page(request):
  return render(request,'faculty/my_portfolio_page.html')


def profile_page(request):
  return render(request,'faculty/profile_page.html')