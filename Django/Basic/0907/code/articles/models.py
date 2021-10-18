from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)  # max_length는 필수
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # django가 자동으로 넣어주는 값/ 입력 받을 수 없고 수정 x
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title