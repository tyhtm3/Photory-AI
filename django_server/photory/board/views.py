from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from .models import Article
from .serializers import ArticleListSerializer,ArticleDetailSerializer,ArticleSerializer

# Create your views here.

@api_view(['GET'])
def article_list(requset):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(nickname=request.nickname)
        return Response(serializer.data)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def article_update(request):
    if request.method=="PUT":
        article =article.objects.get(nickname = request.nickname)
        try:
            article.bookcover = request.data['bookcover']
            article.story = request.data['story']
            article.title = request.data['title']
            article.writer = request.data['writer']
            article.content = request.data['content']
            article.category = request.data['category']
            article.save()
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status =200)
        except:
            return Response({'status': False})
    else:
        request.article.delete()
        return Response(status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated]) 
def article_delete(request, article_pk):
	article = Article.objects.get(pk = article_pk)
	article.delete()
	return Response(status=200)

def index(request, pagenum,pagenum2):
    articles = Article.objects.order_by('-pk')
    if pagenum2 ==0:
        pagenum2=1
    pages = [i for i in range(1,len(movies)+1)]
    page2 = max(1,min((pages[-1]-1//10,pagenum2)))
    pages= pages[(page2-1)*10:(page2)*10]
    if pagenum<pages[0]:
        pagenum=pages[0]
    elif pagenum>pages[-1]:
        pagenum=pages[-1]
    return Response()