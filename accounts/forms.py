from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

attrs = {"class": "form-control"}


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label="UserName", widget=forms.TextInput(attrs=attrs))

    password = forms.PasswordInput(attrs=attrs)


class userregistrationform(UserCreationForm):
    first_name = forms.CharField(
        label="first name",
        widget=forms.TextInput(attrs=attrs)
    )
    last_name = forms.CharField(
        label="last name",
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(attrs=attrs)
    )
    email = forms.EmailField(
        label="email",
        widget=forms.TextInput(attrs=attrs))

    password1 = forms.CharField(
        label="Password", strip=False, widget=forms.TextInput(attrs=attrs))
    password2 = forms.CharField(
        label="Password Confirmation", strip=False, widget=forms.TextInput(attrs=attrs))

    class Meta(UserCreationForm.Meta):
        fields = ("first_name", "last_name", "username", "email")

class Profile_Form(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }