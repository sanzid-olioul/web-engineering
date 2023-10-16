from django.urls import path
from .views import UserLogin,UserLogout,UserRegister,UserEdit,Profile
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(Profile.as_view(),login_url='user_login'),name='user_profile'),
    path('edit',UserEdit.as_view(),name='edit_user'),
    path('login',UserLogin.as_view(),name='user_login' ),
    path('register', UserRegister.as_view(),name='user_register'),
    path('logout', login_required(UserLogout.as_view()),name='user_logout'),
]