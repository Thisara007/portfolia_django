
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('projects',views.project,name="project"),
    path('certification',views.certification,name="certification"),
    path('resume',views.resume,name="resume"),
    path('contact',views.contact,name="contact") 
]
