from django.shortcuts import render
# 장고는 명시적 상대경로 (.)같은 위치에 있다
from .models import Article


# Create your views here.
def index(request):
    # 작성된 모든 게시글을 출력
    # 1. 모든 게시글 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # new로부터 tiltle과 content 받아서 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 1
    # article = Article()
    # article.title = title   #오른쪽 타이틀이 위에 있는 타이틀..
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()
    # 3 : 저장 전에 오류 확인 불가
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')


def detail(request, pk):
    pass


def delete(request, pk):
    pass


def edit(request, pk):
    pass


def update(request, pk):
    pass
