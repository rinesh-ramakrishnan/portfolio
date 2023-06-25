from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def linkedinView(request):
    return redirect('https://www.linkedin.com/in/rinesh-ramakrishnan')

def gitHubView(request):
    return redirect('https://www.github.com/rinesh-ramakrishnan')

def twitterView(request):
    return render(request, 'page_not_found.html')

def facebookView(request):
    return render(request, 'page_not_found.html')

def credlyView(request):
    return redirect('https://www.credly.com/users/rinesh-ramakrishnan')
