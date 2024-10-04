from django.shortcuts import render

# Create your views here.

def homePage(request):
  return render(request,'qao/home_page.html')

def filespage(request):
  return render(request,'qao/files_page.html')

def myprofile(request):
  return render(request,'qao/profile_page.html')