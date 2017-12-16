from django.shortcuts import render
from datetime import datetime
from .models import Article

def main(request):
    context = {
        'datetime':datetime.now(),
        'title':'Main'
    }
    return render(request, 'main.html', context)

def profile(request):
    context = {
        'datetime':datetime.now(),
        'title':'Profile'
    }
    return render(request, 'profile.html', context)

def news(request):
    context = {
        'datetime':datetime.now(),
        'title':'News'
    }
    return render(request, 'news.html', context)

def posts(request):
    populate_db()
    articles=get_articles()
    context = {
        'articles':articles,
        'datetime':datetime.now(),
        'title':'Posts'
    }
    return render(request, 'posts.html', context)

def get_articles():
    result = Article.objects.all()
    return result


def populate_db():
    if Article.objects.count() == 0:
        Article(title='first post', post='this is first post').save()
        Article(title='second post', post='this is second post').save()