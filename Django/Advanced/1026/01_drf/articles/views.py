from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404, render

from .models import Article
from .serializers import ArticleListSerializer
from articles import serializers

# Create your views here.

@api_view(['GET'])
def article_list(request):
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)