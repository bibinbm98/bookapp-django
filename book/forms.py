from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Insertbookform(forms.Form):
    book_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))
    author = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))
    pages = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))
    price = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'Book_name': forms.TextInput(attrs={"class": "form-control"}),
            'Author': forms.TextInput(attrs={"class": "form-control"}),
            'Pages': forms.TextInput(attrs={"class": "form-control"}),
            'Price': forms.TextInput(attrs={"class": "form-control"}),
        }


class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.TextInput(attrs={"class": "form-control"}),
            'password2': forms.TextInput(attrs={"class": "form-control"}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
