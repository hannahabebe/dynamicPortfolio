from dataclasses import fields
import imp
from multiprocessing import context
from django.shortcuts import render

from base.forms import ContactForm
from .models import mySkill, service, contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.

def homePage(request):
    skills = mySkill.objects.all()
    services = service.objects.all()

    context = {'services': services, 'skills': skills}

    return render(request, 'base/index.html', context)

def contactPage(CreateView):
    model = contact
    # fields = ["fName", "lName", "country", "message"]
    form_class = ContactForm
    success_url = reverse_lazy("thanks")

def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")

