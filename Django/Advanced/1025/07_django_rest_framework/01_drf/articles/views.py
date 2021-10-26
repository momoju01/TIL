from django.db import reset_queries
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from articles import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # raise exception 쓰면 삭제

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터{article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_COMMENT)
