from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django import template
from .models import News
from .forms import NewsForm


def index(request):
    return render(request, "index.html")
def news(request):
    return render(request, "news.html")
def guids(request):
    return render(request, "guids.html")
def matches(request):
    return render(request, "matches.html")
def tournaments(request):
    return render(request, "tournaments.html")
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # перенаправление на страницу списка новостей
    else:
        form = NewsForm()
    return render(request, 'news_create.html', {'form': form})
def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news.html', {'news_list': news_list})
def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news': news})