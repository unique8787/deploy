from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
@login_required
def book(request):
    if request.method == "POST":
        bn = request.POST.get("book_name")
        bd = request.POST.get("book_description")
        bi = request.FILES.get("book_image")
        Book.objects.create(book_name = bn,book_description = bd, book_image = bi)
        return redirect("/")
    queryset = Book.objects.all()
    context = {'books':queryset}
    return render(request,"books.html",context)

@login_required(login_url = '/login/')
def delete_book(request,id):
    data = Book.objects.get(id=id)
    data.delete()
    return redirect('/')
@login_required(login_url = '/login/')
def update_book(request,id):
    queryset = Book.objects.get(id=id)
    if request.method == "POST":
        bn = request.POST.get('book_name')
        bd = request.POST.get('book_description')
        bi = request.FILES.get('book_image')
        queryset.book_name = bn
        queryset.book_description = bd
        if bi:
            queryset.book_image = bi
        queryset.save()
        return redirect('/')
    context = {'book':queryset}
    return render(request,'updatebooks.html',context)

from django.contrib.auth.models import User
from django.contrib import messages

def register_page(request):
    if request.method == 'POST':
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        un = request.POST.get('username')
        em = request.POST.get('email')
        pw = request.POST.get('password')
        if not fn or not ln or not un or not em or not pw:
            messages.error(request,"All fields are mandatory")
            return redirect('/register/')
        if User.objects.filter(username = un).exists():
            messages.error(request,"User already exitst")
            return redirect('/register/')
        User.objects.create_user(first_name = fn, last_name = ln, username = un, email = em, password = pw)
        messages.success(request,"New user created successfully")
        return redirect('/login/')

    return render(request,'register.html')
from django.contrib.auth import authenticate , login, logout
def login_page(request):
    if request.POST:
        un = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(username = un, password = pw)
        if user is None:
            messages.error(request, "Invalid credentials")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
