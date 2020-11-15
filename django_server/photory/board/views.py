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
    articles = Article.objects.order_by('-pk')
    serializer = ArticleListSerializer(articles[:8], many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_count(request):
    article_count = Article.objects.count()
    return Response(article_count)
    
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
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE','PUT'])
@permission_classes([IsAuthenticated]) 
def article_delete_update(request, article_pk): 
    if request.method == 'DELETE':
        article = Article.objects.get(pk = article_pk)
        article.delete()
        return Response(status=200)
    else:
        article =Article.objects.get(pk=article_pk)
        article.bookcover = request.data['bookcover']
        article.title = request.data['title']
        article.writer = request.data['writer']
        article.content = request.data['content']
        article.category = request.data['category']
        article.save()
        return Response(status =200)

@api_view(['GET'])
def index(request, pagenum):
    articles = Article.objects.order_by('-pk')
    serializer = ArticleListSerializer(articles[pagenum*8:(pagenum+1)*8], many=True)
    return Response(serializer.data)