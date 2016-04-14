from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def quest(r):
    return render(r, "root.html")

def page_404(r):
    return render(r, "404.html")