from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # 5. create 경로로 요청이 들어옴(POST)/ case1. 잘못된 입력 => 사용자가 데이터를 입력
    # 10. create 경로로 요청이 들어옴(POST)/ case2. 올바른 입력 => 사용자가 데이터를 입력
    if request.method == 'POST':
        # 6. 데이터가 입력된 종이를 가져옴 => ArticleForm 을 인스턴스(빈 종이 + 사용자 데이터)
        # 11. 데이터가 입력된 종이를 가져옴 => ArticleForm 을 인스턴스(빈 종이 + 사용자 데이터)
        form = ArticleForm(data=request.POST) # data는 생략 가능
        # 7. 사용자가 입력한 데이터가 유효한지(올바른지) 확인
        # 12. 사용자가 입력한 데이터가 유효한지(올바른지) 확인
        if form.is_valid():
            # 13. 데이터를 db에 저장한다.
            form.save()    
            # 14. index로 리다이렉트 시켜준다
            return redirect('articles:index')

    else:   # 1. create 경로로 요청이 들어옴 (GET 요청-db에 영향x) => 빈 종이(Form) 응답
        form = ArticleForm()  # 2. ArticleForm 을 인스턴스화 한다 => 빈 종이 생성

    # 3. 사용자에게 빈 종이를 주기 위해서 context에 form을 담는다.
    # 8. 잘못된 데이터를 다시 입력받기 위해 context에 form을 담는다.
    context = { 
        'form': form,
    }
    # 4. 사용자에게 데이터를 받기 위해 빈 종이를 넘겨준다. => 데이터를 입력한다.
    # 9. 사용자에게 올바른 데이터를 받기 위해 form을 넘겨준다.
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article:index')


@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()  # article에 수정 완료된 데이터 한 줄이 들어감
            return redirect('articles:detail', article.pk)
    
    else: # GET요청
        form = ArticleForm(instance=article)

    context = {
        'article': article, # article.pk 에 사용하려고
        'form': form,
    }
    return render(request, 'articles/update.html', context)