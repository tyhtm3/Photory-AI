from django.shortcuts import render,redirect, get_object_or_404
from .models import User
import urllib 

import os,json

from rest_auth.registration.views import SocialLoginView                   
from allauth.socialaccount.providers.kakao import views as kakao_views     
from allauth.socialaccount.providers.oauth2.client import OAuth2Client     
import requests                       
from .serializers import UserSerializer  
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from django.contrib.auth import get_user_model

from .serializers import UserSerializer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# secret_file = os.path.join(BASE_DIR,'Back', 'secrets.json')
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
    
# with open(secret_file) as f:
#     secrets = json.loads(f.read())

# def get_secret(setting, secrets=secrets):
#     """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
#     try:
#         return secrets[setting]
#     except KeyError:
#         error_msg = "Set the {} environment variable".format(setting)
#         raise ImproperlyConfigured(error_msg)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    try:
        user = User.objects.get(email = request.user)
        user.profile = request.data['profile']
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status =200)
    except:
        return Response({'status':False})