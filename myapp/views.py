from django.shortcuts import render

# Create your views here.
def hola_mundo(requets):
    return render(requets, 'hola_mundo.html')