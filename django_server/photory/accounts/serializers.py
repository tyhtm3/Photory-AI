from rest_framework import serializers
from django.contrib.auth import get_user_model

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer

from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','email','nickname','profile']

class RegistrationSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True)
    profile = serializers.ImageField(required=False)

    def get_cleaned_data(self):
        
        return {
            'email' : self.validated_data.get('email', ''),
            'password1' : self.validated_data.get('password1', ''),
            'password2' : self.validated_data.get('password2', ''),
            'profile' : self.validated_data.get('profile', ''),
        }