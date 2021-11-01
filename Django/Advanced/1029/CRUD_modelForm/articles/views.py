from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 1. DB로부터 받은 쿼리셋을 이후에 파이썬이 변경
    # articles = Article.objects.all()[::-1]  
    
    # 2. 처음부터 내림차순 쿼리셋으로 받음(DB가 조작)
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    # 이전 create (작성)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 이전 new (조회)
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

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.mehtod == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
    
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)




""" 이전 
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)

def create(request):
    ## 1. Form쓸때
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    ## 2. ModelForm 쓸 때
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
"""