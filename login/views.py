from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .forms import LoginForm

# Create your views here.
#creating a view for log in and authenticates user
def login_view(request):
  if request.method =="POST":
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)

      if user is not None:
        login(request, user)
        #check user role and redirect them to their dashboard
        if user.role.name =='Dean':
          return redirect(reverse('userManagement'))
        elif user.role.name =='Faculty':
          return redirect(reverse('homepage'))
        
      else:
        form.add_error(None, 'Invalid username or password')  


  else:
    form = LoginForm()

  return render(request, 'login/login.html', {'form':form})




#creating a logout function
def log_out(request):
  logout(request)
  return redirect('login')