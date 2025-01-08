from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def price(request):
    return render(request, 'price.html')