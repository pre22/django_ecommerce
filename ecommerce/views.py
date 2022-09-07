from django.shortcuts import render
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

    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/login.html")

def register_page(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html")
