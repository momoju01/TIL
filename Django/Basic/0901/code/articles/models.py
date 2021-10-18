from django.db import models

# Create your models here.
class Article(models.Model):
    # id 생략된 것
    # id = models.AutoField(primary_key=True) 1, 2, 3, 4, 

    title = models.CharField(max_length=10)  # max_length필수 -> 위젯 (클래스 변수)
    content = models.TextField()  # max_length 옵셔널
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)