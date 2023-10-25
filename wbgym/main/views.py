from django.shortcuts import render
from .models import Article
# Create your views here. These are test views only for dev

def home(request):
    # get all articles
    articles = Article.objects.all()
    
    return render(request, 'main/home.html', {'articles': articles})
