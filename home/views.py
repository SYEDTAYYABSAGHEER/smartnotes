from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = { 'today': datetime.today()}


# def home(request):
#     #return HttpResponse("Hello World!");
#     return render(request,'home/welcome.html',{ 'today': datetime.today()})


# @login_required(login_url="/admin")
# def authroized(request):
#     return render(request,'home/authroized.html',{})


class AuthroizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authroized.html'
    login_url = 'admin'

# Create your views here.
