from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    # 작성한 모든 게시글을 출력
    # 1. 모든 게시글 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    pass


def create(request):
    pass


def detail(request, pk):
    pass


def delete(request, pk):
    pass


def edit(request, pk):
    pass


def update(request, pk):
    pass
