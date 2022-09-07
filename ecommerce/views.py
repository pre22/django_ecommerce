from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from ecommerce.forms import ContactForm, LoginForm

def home_view(request):
    return render(request, "HomePage.html")

def about_view(request):
    return render(request, "AboutPage.html")

def contact_view(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "form": form
    }
    return render(request, "contact/ContactPage.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # context["form"] = LoginForm()
            return redirect("/login")
        else:
            print("Error")


    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html")
