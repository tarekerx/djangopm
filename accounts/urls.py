from django.contrib.auth.views import LoginView
from django.urls import path, include
from accounts.forms import UserLoginForm
from django.contrib.auth.views import LogoutView
from accounts.views import edit_profile

from accounts.views import registerview

urlpatterns = [path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
               path('register/', registerview.as_view(), name='register'),
               path('logout/', LogoutView.as_view(), name='logout'),
                path('profile/', edit_profile, name='profile'),
               path('', include('django.contrib.auth.urls'))]