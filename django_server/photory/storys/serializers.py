from rest_framework import serializers

from .models import Story,BookStory

class StoryListSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Story
        fields = '__all__'
        # fields = ['id','title','images']

class BookStoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStory
        fields = '__all__'
        # fields = ['id','title','images']