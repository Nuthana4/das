from django.shortcuts import render
from django.shortcuts import redirect

def open(request):
    return render(request, "dashboard/index.html")

def main(request):
    return render(request, "dashboard/main.html")

def login(request):
    return render(request, "dashboard/login.html")

def register(request):
    return render(request, "dashboard/register.html")

def profile(request):
    return render(request, "dashboard/profile.html")

def about(request):
    return render(request, "dashboard/about.html")

def contact(request):
    return render(request, "dashboard/contact.html")


def login_view(request):
    if request.method == "POST":
        return redirect("dashboard:main")
    return render(request, "dashboard/login.html")

def register_view(request):
    if request.method == "POST":
        return redirect("dashboard:login")
    return render(request, "dashboard/register.html")

# Landing page pages
def about_landing(request):
    return render(request, "dashboard/about_lan.html")

def contact_landing(request):
    return render(request, "dashboard/contact_lan.html")

# Dashboard pages
def about_dashboard(request):
    return render(request, "dashboard/about_das.html")

def contact_dashboard(request):
    return render(request, "dashboard/contact_das.html")



