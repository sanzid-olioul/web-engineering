from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group,User as AuthUser
from django.contrib.auth import authenticate, login,logout
from django.views import View
from .form import RegisterForm,LoginForm
from .models import UserProfile,User

class UserLogin(View):
    def get(self,request,*args,**kwargs):
        frm = LoginForm()
        return render(request,'user/login.html',{'form':frm})
    
    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password =form.cleaned_data['pasword']
    
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
        return render(request,'user/login.html',{'form':form})

class UserRegister(View):
    def get(self,request,*args,**kwargs):
        frm = RegisterForm()
        return render(request,'user/register.html',{'form':frm})
    
    def post(self,request,*args,**kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date_of_birth = form.cleaned_data['date_of_birth']
            password = form.cleaned_data['password']
            user = User.objects.create_user(email=email,first_name=first_name,\
                                            last_name=last_name,date_of_birth=date_of_birth,password=password)
            # group = Group.objects.get(name='regular')
            # user.groups.add(group)
            user.save()
            return redirect('user_login')
        return render(request,'user/register.html',{'form':form})

class UserLogout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('user_login')
    
class UserEdit(View):
    def get(self,request,*args,**kwargs):
        profile = UserProfile.objects.get(user=request.user)
        return render(request,'user/edit_image.html',{'profile':profile})
    
class Profile(View):
    def get(self,request,*args,**kwargs):
        # only get request will be handled to the authenticate user.
        user = request.user
        profile = UserProfile.objects.get(user=user)
        cover_photo = './icon/cover-avater.jpg'
        return render(request,'user/profile.html',{'profile':profile,'cover_photo':cover_photo})