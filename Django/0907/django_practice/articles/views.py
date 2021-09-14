from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

## 구 new 함수
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

## 구 create 함수
# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('overview')
#     form = Article(title=title, content=content)
#     form.save()
#     return redirect('articles:index')

## 새로운 create 함수
# def create(request):
#     form = ArticleForm(request.POST)
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     return redirect('articles:new')


# new 함수와 create 함수 합치기
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
         form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
         form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/create.html', context)