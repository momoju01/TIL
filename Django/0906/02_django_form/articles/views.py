from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form. is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        # new 
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)



@require_http_methods(['GET', 'POST'])
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article= get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)



@require_POST
def delete(request, pk):
    # article = Article.objects.get(pk=pk)
    article= get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')


  

def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article= get_object_or_404(Article, pk=pk)
    # update
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # edit
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

