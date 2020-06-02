from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):

    homes = home.objects.all()
    social = socialconnect.objects.all()
    sidebar = sidenavbar.objects.all()
    us = about.objects.all()
    edu = education.objects.all()
    skill = skills.objects.all()
    certi = certificate.objects.all()
    sol = solution.objects.all()
    pro = project.objects.all()
    con = contact.objects.all()
    sub = subscribe.objects.all()
    

    return render(request,"index-particle.html",{
        'homes': homes, 
        'social': social, 
        'sidebar' : sidebar,
        'about' : us,
        'education' : edu,
        'skills' : skill,
        'certificate' : certi,
        'solution' : sol,
        'project' : pro,
        'contact' : con,
        'subscribe' : sub,

        })


    

    



    