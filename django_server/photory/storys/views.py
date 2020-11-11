from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import StoryListSerializer
from .models import Story,Images
import requests
# Create your views here.
 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def storys(request):
    storys = Story.objects.filter(user = request.user)
    serializer = StoryListSerializer(storys, many=True)
    return Response(serializer.data)
    # for i in storys:
    #     i.delete()
    # return Response(1)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def story_detail(request,story_pk):
    story = get_object_or_404(Story, pk=story_pk)
    return Response(story)

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
            story.content0 = "초기 내용을 받아오는 중입니다."
            story.save()
            con['status'] = True
            con['pk'] = story.pk
            return Response(con)
        except:
            return Response({'status':False})

@api_view(['POST'])
def ai_receive(request):
    #     data={
    # story_pk:num ,
    # imagePath:string,
    # contents:[string,...]
    # }
    story = get_object_or_404(Story, pk=request.data['story_pk'])
    imgs = story.images.all()
    imgs = list(story.images.all())
    imgs = list(map(str,imgs))
    imgs.sort()
    for i in range(5):
        story.content =  '<img id="mainImg" class="normImg" draggable="false" src="'+imgs[i] + '" style="position:absolute;left:0px;top:0px;width:30%;height:30%;"/><div id="con1" class="contentt" draggable="false" style="position:absolute;left:0px;top:0px;width:30%;height:30%;z-index:100;"><p>' + request.data['contents'][i] + '</p></div>'
    story.editable = True
    return Response({'status':"OK"})

@api_view(['GET'])
def get_normImg(request,story_pk,img_num):
    story = get_object_or_404(Story, pk=story_pk)
    imgs = list(story.images.all())
    imgs = list(map(str,imgs))
    imgs.sort()
    return Response({'status':"OK",'img':"http://127.0.0.1:8000/media/"+imgs[img_num]})

@api_view(['PUT'])
def storys_u(request):
    con = {}
    if request.method == "PUT":
        try:
            story = get_object_or_404( Story ,pk = request.data['id'])
            story.title = request.data['title']
            story.writer = request.data['writer']
            story.content0 = request.data['content0']
            story.content1 = request.data['content1']
            story.content2 = request.data['content2']
            story.content3 = request.data['content3']
            story.content4 = request.data['content4']
            story.complete = request.data['complete']
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
        con['content']=[
            story.content0,
            story.content1,
            story.content2,
            story.content3,
            story.content4
        ]
        con['complete']=story.complete
        con['editable']=story.editable
        con['create_at']=story.create_at
        con['update_at']=story.update_at
        con['image']=[str(i.image) for i in story.images.all()]
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
        # 
        if len(story.images.all())==5:
            url = 'http://121.125.56.92:50740/tale'
            data = {
                'story_pk':story_pk,
                'imagePaths':[str(i.image) for i in story.images.all()]
            }
            print(data)
            requests.post(url,data=data)
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