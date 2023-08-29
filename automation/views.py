# chat/views.py
from django.shortcuts import render

def automation(request):
    return render(request, "automation/automation.html")
