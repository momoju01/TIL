from django.shortcuts import redirect, render

# Create your views here.

def index(request):

    return render(request, 'articles/index.html')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def edit(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'artricle': article,
    }
    return redirect(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)