from rest_framework import serializer
from .models import Article

class ArticleListSerializer(serializer.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title',)