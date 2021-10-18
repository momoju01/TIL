from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

def articles_image_path(instance, filename):
    return f'user_{instance.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    # image = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
    # image = models.ImageField(upload_to=articles_image_path, blank=True)

    # 썸네일 이미지 만듦. 원본 이미지를 가공하여 넣기 때문에, 원본은 저장x 썸네일만 저장)
    # image_thum = ProcessedImageField(
    #     blank=True,
    #     upload_to='thumbnails/',
    #     processors=[ResizeToFill(100, 50)],
    #     format='JPEG',
    #     options={'quality':60},
    #     ) 

    # 원본(o) 썸네일(o)
    image = models.ImageField(upload_to='origins/', blank=True)
    image_thumbnail = ImageSpecField(
        source = 'image',  # 원본 이미지 필드 명
        processors=[ResizeToFill(100,50)],
        options={'quality': 90},
    )  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
