from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Department, Role


# The dean can create a faculty user and that user's department is automatically set to the dean's department
class CustomUserCreationForm(UserCreationForm):
  department = forms.ModelChoiceField(queryset=Department.objects.all(),required=True, disabled=True)
  
  address = forms.CharField(widget=forms.Textarea, required=True)
  username = forms.CharField(max_length=50, required=True)
  email = forms.EmailField(required=True)
  first_name = forms.CharField(required=True)
  last_name = forms.CharField(required=True)


  class Meta:
    model = CustomUser
    fields =('username','first_name','last_name','email','department','role','address','password1','password2')

  def __init__(self, *args, **kwargs):
    self.dean = kwargs.pop('dean',None)
    super().__init__(*args,**kwargs)
    if self.dean:
      self.fields['department'].initial = self.dean.department
      self.fields['department'].queryset=Department.objects.filter(id=self.dean.department.id)
      self.fields['role'].initial = Role.objects.get(name='Faculty')
      self.fields['role'].queryset = Role.objects.filter(name='Faculty')

  def save(self, commit=True):
    user = super().save(commit=False)
    if self.dean:
      user.department = self.dean.department
      user.role = Role.objects.get(name='Faculty')  #automatically set the role to faculty

    if commit:
      user.save()
    return user