"""photory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#JWT
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from allauth.account.views import confirm_email


urlpatterns = [
    path('admin/', admin.site.urls),

    #My apps
    path('storys/', include('storys.urls')),
    path('board/', include('board.urls')),

    ## django rest-auth API
    path('rest-auth/', include('rest_auth.urls')), # login&logout
    path('rest-auth/signup/', include('rest_auth.registration.urls')),# signup

    # #Email 인증
    # path('accounts/', include('allauth.urls')),
        
    # #Google 로그인
    # path('auth/',include('accounts.urls')),
    
    # #JWT
    # path('api-jwt-auth/', obtain_jwt_token),
    # path('api-jwt-auth/refresh/',refresh_jwt_token),
    # path('api-jwt-auth/verify/',verify_jwt_token),

]
