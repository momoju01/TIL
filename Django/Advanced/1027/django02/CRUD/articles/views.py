from django.shortcuts import redirect, render
from .models import Article

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

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # new로부터 title과 content 받아서 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 데이터 저장하는 방법
    # # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # # 3
    # Article.objects.create(title=title, content=content)
    
    # 2
    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)

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