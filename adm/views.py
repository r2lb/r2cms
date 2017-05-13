from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'adm/base.html', {})

def dashboard2(request):
    return render(request, 'adm/index2.html', {})

def test(request):
    return render(request, 'adm/test.html', {})
