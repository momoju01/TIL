from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .serializers import ArticleSerializer
from .models import Article

# 1. HTML response
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
 
# 2. JsonResponse
# from django.http.response import JsonResponse
def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []
 
    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)  # dict 이외의 객체 직렬화 하려면 False로 설정해야함


# 3. Django Serializer
# 주어진 모델 정보 활용하기 때문에 이전과 달리 필드를 개별적으로 직접 만들어 줄 필요 x
# from django.http.response import JsonResponse, HttpResponse
# from django.core import serializers
def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)  # 타입 결정, 보낼 데이터
    return HttpResponse(data, content_type='application/json')  # render 안 함! http 응답 주는 것


# 4.Django REST Framework
# @api_view(['GET'])
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import ArticleSerializer
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)  # 모델폼과 형식 같음(#쿼리셋(데이터), many=True)
    return Response(serializer.data)    # 응답하는 것 : 응답 객체 생성 -> serializer의 데이터