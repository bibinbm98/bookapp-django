from django.shortcuts import render,redirect
from book.forms import Insertbookform,BookUpdateForm,UserRegisterationForm,LoginForm
from .models import Book
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_required(func):
    def wrapper(request,id=None):
        if not request.user.is_authenticated:
            return redirect("loginview")
        else:
            return func(request,id)
    return wrapper

def create_book(request):
    context={}
    form=Insertbookform()
    context["form"]=form
    if request.method=="POST":
        form=Insertbookform(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data.get("book_name")
            author = form.cleaned_data.get("author")
            pages = form.cleaned_data.get("pages")
            price = form.cleaned_data.get("price")
            book=Book(Book_name=book_name,Author=author,Pages=pages,Price=price)
            book.save()
            print("books r saved")
        return redirect("listbook")
    return render(request,"book/createbook.html",context)

def list_all_book(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"book/listallbooks.html",context)

def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("listbook")

def update_book(request,id):
    book=Book.objects.get(id=id)
    form=BookUpdateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookUpdateForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbook")
    return render(request,"book/update.html",context)

def Registration(request):
    form=UserRegisterationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginview")
        else:
            context["form"]=form
            return render(request,"book/registeration.html",context)
    return render(request,"book/registeration.html",context)

def login_todo(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"book/home.html")
            else:
                context["form"]=form
                return render(request,"book/login.html",context)


    return render(request,"book/login.html",context)

def django_logout(request):
    logout(request)
    return redirect("loginview")