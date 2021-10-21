from django.db import models
from django.conf import settings
from django.db.models.fields import related

# Create your models here.
class Article(models.Model):
    # user(1) -> article(N)
    # user는 여러 article에 좋아요 누를 수 있다
    # article은 여러 user로 부터 좋아요를 받을 수 있다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 여기선 settings.AUTH_USER_MODEL, 딴데선 get_user_model
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')  # 자동으로 중개테이블 만듦
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
