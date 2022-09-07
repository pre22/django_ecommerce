from django.shortcuts import render
from ecommerce.forms import ContactForm

def home_view(request):
    return render(request, "HomePage.html")

def about_view(request):
    return render(request, "AboutPage.html")

def contact_view(request):
    return render(request, "contact/ContactPage.html")