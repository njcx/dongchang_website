# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'interest_home.html')
