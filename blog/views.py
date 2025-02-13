from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})