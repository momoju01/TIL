from django.http import response
from django.shortcuts import get_list_or_404, get_object_or_404, render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from music.serializers import ArtistListSerializer
from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def artist_list(request):
    # GET 요청인 경우 모든 가수의 id와 name 컬럼을 JSON으로 응답한다.
    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        serializers = ArtistListSerializer(artists, many=True)
        return Response(serializers.data)
    # POST 요청인 경우 가수의 정보를 생성한다.
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)


@api_view(['GET'])
def music_list(request):
    musics = get_list_or_404(Music)
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):

    music = get_list_or_404(Music, pk=music_pk)

    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        data = {
            'message': f'{music_pk}번 음악이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MusicSerializer(instance=music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)