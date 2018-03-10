from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'landing_page.html')

def books(request):
    return render(request, 'books.html')

def mining(request):
    return render(request, 'mining.html')

def charting(request):
    return render(request, 'charting.html')

def lending(request):
    return render(request, 'lending.html')