from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_safe
from .models import Movie
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)  # 전체 쿼리셋 10개씩 잘라서 
    
    # 몇 페이지 보여줄 것인지
    page_number = request.GET.get('page') # 정보는 request안에 GET 이라는 url parameter 안에 들어있는 값 가져올것
    page_obj = paginator.get_page(page_number) # 몇 번 page인지 정보

    # /movies/?page=2 ajax 요청 => json데이터로 받기
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # 지금 이 요청은 ajax요청입니다
        data = serializers.serialize('json', page_obj)  #page_obj를 json으로 바꿔줘
        return HttpResponse(data, content_type='application/json')
        
    # /movies/ 첫번째 페이지 요청 
    else:
        
        context = {
            # 'movies': movies,  # 전체
            'movies': page_obj,
        }
        return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    pass

@require_safe
def recommended(request):
    pass