from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import StoryListSerializer,BookStoryListSerializer
from .models import Story,Images,BookStory
import requests, json
# Create your views here.
 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def storys(request):
    storys = Story.objects.filter(user = request.user)
    serializer = StoryListSerializer(storys, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def storys_init(request):
    con={}
    tmp=[]
    if request.method == "POST":
        try:
            tmp.append('1')
            story = Story()
            tmp.append('2')
            story.user = request.user
            tmp.append('3')
            story.title = "제목을 입력해 주세요"
            story.writer = "지은이를 입력해 주세요"
            story.content0 = "초기 내용을 받아오는 중입니다."
            story.save()
            tmp.append('4')

            con['status'] = True
            con['pk'] = story.pk
            return Response(con)
        except:
            con['data'] = tmp
            con['status'] = False
            return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_init(request):
    con={}
    if request.method == "POST":
        # try:
        bstory = BookStory()
        bstory.user = request.user
        bstory.title = request.data['title']
        bstory.writer = request.data['writer']
        bstory.content0 = request.FILES['c0']
        bstory.content1 = request.FILES['c1']
        bstory.content2 = request.FILES['c2']
        bstory.content3 = request.FILES['c3']
        bstory.content4 = request.FILES['c4']
        bstory.save()
        con['status'] = True
        con['pk'] = bstory.pk
        return Response(con)
        # except:
        #     return Response({'status':False})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def books(request):
    bstorys = BookStory.objects.filter(user = request.user)
    serializer = BookStoryListSerializer(bstorys, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ai_receive(request):
    #     data={
    # story_pk:num ,
    # imagePath:string,
    # contents:[string,...]
    # }
    data = dict(request.data)
    story = get_object_or_404(Story, pk=data['story_pk'][0])
    imgs = story.images.all()
    imgs = list(story.images.all())
    imgs = list(map(str,imgs))
    imgs.sort()
    story.content0 =  '<img id="mainImg" class="normImg" draggable="false" src="http://k3a205.p.ssafy.io:8000/media/'+imgs[0] + '" style="position:absolute;left:0px;top:0px;width:30%;height:30%;"/><div id="con1" class="contentt" draggable="false" style="position:absolute;left:0px;top:0px;width:30%;height:30%;z-index:100;"><p>' + data['tale'][0] + '</p></div>'
    story.content1 =  '<img id="mainImg" class="normImg" draggable="false" src="http://k3a205.p.ssafy.io:8000/media/'+imgs[1] + '" style="position:absolute;left:0px;top:0px;width:30%;height:30%;"/><div id="con1" class="contentt" draggable="false" style="position:absolute;left:0px;top:0px;width:30%;height:30%;z-index:100;"><p>' + data['tale'][1] + '</p></div>'
    story.content2 =  '<img id="mainImg" class="normImg" draggable="false" src="http://k3a205.p.ssafy.io:8000/media/'+imgs[2] + '" style="position:absolute;left:0px;top:0px;width:30%;height:30%;"/><div id="con1" class="contentt" draggable="false" style="position:absolute;left:0px;top:0px;width:30%;height:30%;z-index:100;"><p>' + data['tale'][2] + '</p></div>'
    story.content3 =  '<img id="mainImg" class="normImg" draggable="false" src="http://k3a205.p.ssafy.io:8000/media/'+imgs[3] + '" style="position:absolute;left:0px;top:0px;width:30%;height:30%;"/><div id="con1" class="contentt" draggable="false" style="position:absolute;left:0px;top:0px;width:30%;height:30%;z-index:100;"><p>' + data['tale'][3] + '</p></div>'
    story.content4 =  '<img id="mainImg" class="normImg" draggable="false" src="http://k3a205.p.ssafy.io:8000/media/'+imgs[4] + '" style="position:absolute;left:0px;top:0px;width:30%;height:30%;"/><div id="con1" class="contentt" draggable="false" style="position:absolute;left:0px;top:0px;width:30%;height:30%;z-index:100;"><p>' + data['tale'][4] + '</p></div>'
    story.editable = True
    story.save()
    return Response({'status':"OK"})

@api_view(['GET'])
def get_normImg(request,story_pk,img_num):
    story = get_object_or_404(Story, pk=story_pk)
    imgs = list(story.images.all())
    imgs = list(map(str,imgs))
    imgs.sort()
    return Response({'status':"OK",'img':"http://k3a205.p.ssafy.io:8000/media/"+imgs[img_num]})

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
            print(story.content0)
            return Response(con)
        except:
            return Response({'status':False})

@api_view(['GET'])
def bookdetail(request,bstory_pk):
    con = {
    }
    if request.method == "GET":
        bookStory = get_object_or_404( BookStory ,pk = bstory_pk)
        con['title']=bookStory.title
        con['writer']=bookStory.writer
        con['content']=[
            bookStory.content0,
            bookStory.content1,
            bookStory.content2,
            bookStory.content3,
            bookStory.content4
        ]
        con['create_at']=bookStory.create_at
        return Response(con)

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
        story = get_object_or_404( Story ,pk = story_pk)
        try:
            story.delete()
            con['status'] = True
        except:
            con['status'] = False
        return Response(con)

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
            err=[]
            try:    
                url = 'http://121.125.56.92:50740/tale'
                url2 = 'http://121.125.56.92:50741/tale'
                data = {
                    'story_pk':story_pk,
                    'imagePaths': sorted([str(i.image) for i in story.images.all()])
                }
                err+=[0]
                requests.post(url,data=json.dumps(data))
                err+=[1]
                requests.post(url2,data=json.dumps(data))
                err+=[2]
                last = True
            except:
                con = {
                    'status':False,
                    'path':err,
                    'last':last
                }
                return Response(con)
        con = {
            'status':True,
            'path':images.image.path,
            'last':last
        }
        return Response(con)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def images_delete(request,image_pk):
    if request.method == "DELETE":
        images = get_object_or_404(Images, pk = image_pk)
        images.delete()
        con = {
            'status':True,
        }
        return Response(con)