from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def project(request):
    return render(request, "projects.html")

def contact(request):
    return render(request, "contact.html")

def send_email(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        from_email = 'bandilenk7@gmail.com'
        send_mail(f'Message from my portfolio from {name}, {email}', message, 'settings.EMAIL_HOST_USER', [from_email], fail_silently=False)
    return redirect('portfolio:home')
