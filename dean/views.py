from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser


# Create your views here.
def home_page(request):
  return render(request,'dean/home.html')


def files(request):
  return render(request,'dean/files.html')


def archive(request):
  return render(request,'dean/archive.html')


def my_profile(request):
  return render(request,'dean/myprofile.html')


# this view renders the list of users in the system but excluding the dean, qao, and the superadmin and users must be on the same department as the dean
def userManagement(request):
  excluded_roles = [1,4]
  users = CustomUser.objects.exclude(role__in=excluded_roles).exclude(is_staff=True)
  dean=request.user
  department = dean.department
  return render(request, 'dean/userManagement.html', {'users':users, 'department':department})



@login_required
def createUser(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST, dean=request.user)
    if form.is_valid():
      form.save()

      
    
      return redirect('userManagement')
    
    else:
      form.add_error(None, 'Invalid')
    
  else:
    form = CustomUserCreationForm(dean=request.user) 
  

  return render(request, 'dean/create_user.html', {'form':form}) 