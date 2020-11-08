from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import StoryListSerializer
from .models import Story,Images
# Create your views here.
 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def storys(request):
    storys = Story.objects.filter(user = request.user)
    serializer = StoryListSerializer(storys, many=True)
    for i in serializer.data:
        print(i)
    return Response(serializer.data)
    # for i in storys:
    #     i.delete()
    # return Response(1)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def storys_init(request):
    con={}
    if request.method == "POST":
        try:
            story = Story()
            story.user = request.user
            story.title = "제목을 입력해 주세요"
            story.writer = "지은이를 입력해 주세요"
            story.content = "초기 내용을 받아오는 중입니다."
            story.save()
            con['status'] = True
            con['pk'] = story.pk
            return Response(con)
        except:
            return Response({'status':False})

@api_view(['PUT'])
def storys_u(request):
    con = {}
    if request.method == "PUT":
        try:
            story = get_object_or_404( Story ,pk = request.data['id'])
            story.title = request.data['title']
            story.writer = request.data['writer']
            story.content = request.data['content']
            story.save()
            con['status'] = True
            con['pk'] = story.pk
            return Response(con)
        except:
            return Response({'status':False})

@api_view(['GET','DELETE'])
def story_rd(request,story_pk):
    con = {
    }
    if request.method == "GET":
        story = get_object_or_404( Story ,pk = story_pk)
        con['title']=story.title
        con['writer']=story.writer
        con['content']=story.content
        con['create_at']=story.create_at
        con['update_at']=story.update_at
        con['image']=[i.image.path for i in story.images.all()]
        return Response(con)
    elif request.method == "DELETE":
        # if request:
        story = get_object_or_404( Story ,pk = story_pk)
        try:
            story.delete()
            con['status'] = True
        except:
            con['status'] = False
        return Response(con)
        # else:
        #     con['status'] = False
        #     con['data'] ="로그인이 필요합니다."
        #     return Response(con)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def images_create(request,story_pk):
    if request.method == "POST":
        story = get_object_or_404( Story ,pk = story_pk)
        images = Images()
        images.user = request.user
        images.story = story
        images.imageName = request.data['fileName']
        images.image = request.FILES['file']
        images.save()
        last = False
        if images.imageName[-1]=="4":
            last = True
        con = {
            'status':True,
            'path':images.image.path,
            'last':last
        }
        return Response(con)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def images_delete(request,image_pk):
    if request.method == "DELETE":
        images = get_object_or_404(Images, pk = image_pk)
        images.delete()
        con = {
            'status':True,
        }
        return Response(con)