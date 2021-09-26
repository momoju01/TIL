# PJT 06

**bold**체는 snippet 단축키





### base.html 에서의 url mapping 
`include('accounts.urls')` : appname 'accounts'의 urls.py로 mapping

```python 
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('admin/', admin.site.urls),
]
```

- pjt_urls(**pu**)
- app_urls(**au**)





### views.py에서 경로 상세히 지정해주기  : views/index(**vi**)

`'community/index.html'` : community 안의 index.html

```python
@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)
```





### forms

- model form  안 썼을 때(**bf**)

```python
from django import forms
from .models import Review

# ModelForm 안 썼을 때 form
class ReviewForm(forms.Form):
    RANK_5 = '5'
    RANK_4 = '4'
    RANK_3 = '3'
    RANK_2 = '2'
    RANK_1 = '1'
    RANK_CHOICES = [
        (RANK_5, '5'),
        (RANK_4, '4'),
        (RANK_3, '3'),
        (RANK_2, '2'),
        (RANK_1, '1'),
    ]
    movie_title = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    # rank = forms.IntegerField()
    rank = forms.ChoiceField(choices=RANK_CHOICES, widget=forms.Select())
```



- ModelForm 썼을 때(**mf**)

```python
from django import forms
from .models import Review

# ModelFrom
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
```





### models.py

- return 값 : `return f'{title} : {movie_title}'`
- models(**models**)

```python
from django.db import models

# Create your models here.

class Review(models.Model):
    movie_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{title} : {movie_title}'
```



### views/create 함수

- 전체 create 함수 : views_create_all(**vca**)

- modelfrom 쓰는 가장 최근 create 함수 : views_create(**vca**)

```python
# 유효성 검사한 create 함수
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)
```



- create_html (**ch**)

```python
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'community:create' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <input type="submit" value="작성">
  </form>
  <a href="{% url 'community:index' %}">[back]</a>
{% endblock content %}

```





### views.detail

- views.detail(**vd**)

```python
@require_safe
def detail(request, pk):
    # review = Review.objects.get(pk=pk)
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'community/detail.html', context)
```

- detail.html(**dh**)

```python
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ review.pk }} 번째 리뷰</h3>
  <hr>
  <p>리뷰 영화 : {{ review.movie_title }}</p>
  <p>리뷰 제목 : {{ review.title }}</p>
  <p>평점 : {{ review.rank }}</p>
  <p>내용 : {{ review.content }}</p>
  <p>작성시각 : {{ review.created_at }}</p>
  <p>수정시각 : {{ review.updated_at }}</p>
  <hr>
  <a href="{% url 'community:update' review.pk %}">[UPDATE]</a>
  <form action="{% url 'community:delete' review.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
  </form>

  
  <a href="{% url 'community:index' %}">[back]</a>
{% endblock content %}

```





### views.update

- views.update(**vu**)

```python
@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # review = Review.objects.get(pk=pk)
    review = get_object_or_404(Review, pk=pk)
    if request.method =='POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'review': review,
        'form':form,
    }
    return render(request, 'community/update.html', context)

```





## Q&A

1. views.py의 create 함수와 update 함수 차이 (인강 보기)

   create 함수: 

   ```python
   @login_required
   @require_http_methods(['GET', 'POST'])
   def create(request):
       if request.method == 'POST':
           form = ReviewForm(request.POST)
           i 
    form.is_valid():
               review = form.save()
               return redirect('community:detail', review.pk)
       else:
           form = ReviewForm()
       context = {
           'form': form,
       }
       return render(request, 'community/create.html', context)
   ```

   update 함수:

   ```python
   @login_required
   @require_http_methods(['GET', 'POST'])
   def update(request, pk):
       review = get_object_or_404(Review, pk=pk)
       if request.method == 'POST':
           form = ReviewForm(request.POST, instance=review)
           if form.is_valid():
               form.save()
               return redirect('community:detail', review.pk)
       else:
           form = ReviewForm(instance=review)
       context = {
           'review': review,
           'form': form,
       }
       return render(request, 'community/update.html', context)
   ```

   