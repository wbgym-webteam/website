from django.shortcuts import render

# Create your views here. These are test views only for dev

def home(request):
    return render(request, 'main/home.html')
