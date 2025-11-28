from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Person


# Create your views here.


def Index_views(request):
    return render(request, "index.html")


def Registration_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("psw")
        password2 = request.POST.get("psw-repeat")

        # 1️⃣ Parollar mosligini tekshirish
        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # 2️⃣ Username bandligini tekshirish
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken!")
            return redirect("register")

        # 3️⃣ Email band bo‘lsa
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered!")
            return redirect("register")

        # 4️⃣ Foydalanuvchini yaratish
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Successfully registered!")

        # 🔥 Registratsiyadan keyin LOGIN sahifasiga o‘tish
        return redirect("login")

    return render(request, "register.html")


def Login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('psw')

        # 🔥 authenticate ichida parol "password" bo'lishi kerak
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Username yoki parol noto‘g‘ri!")
            return redirect('login')
        else:
            login(request, user)
            messages.success(request, "Muvaffaqiyatli login qilindi!")
            return redirect('register')

    return render(request, "login.html")


def Logout_views(request):
    logout(request)
    messages.success(request, "Siz muvaffaqiyatli chiqdingiz!")
    return redirect('login')





