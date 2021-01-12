from django.shortcuts import render
from .models import Article

def index(request):
    a_list = Article.objects.all()
    context = {'article_list': a_list}
    template = 'news/index.html'
    return render(request, template, context)

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year = year)
    context = {'year': year, 'article_list': a_list}
    template = 'news/year_archive.html'
    return render(request, template, context)
