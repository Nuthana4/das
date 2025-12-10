from django.urls import path
from . import views
from django.urls import include

app_name = "dashboard"

urlpatterns = [
    path('', views.open, name='index'),
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('syllabus/', include('syllabus.urls')),
    path('notes/', include('notes.urls')),
    path('papers/', include('papers.urls')),
    
    path('about/', views.about_landing, name='about_lan'),
    path('contact/', views.contact_landing, name='contact_lan'),

    # Dashboard
    path('dashboard/about/', views.about_dashboard, name='about_das'),
    path('dashboard/contact/', views.contact_dashboard, name='contact_das'),


]
