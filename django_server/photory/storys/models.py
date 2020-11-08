from django.db import models
from django.conf import settings

# Create your models here.

class Story(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)


# 이미지 모델
def img_path(instance, filename):
    return "story%s/%s.%s"%(instance.story.pk,instance.imageName,filename.split('.')[-1])
class Images(models.Model):
    story = models.ForeignKey(Story,on_delete=models.CASCADE,related_name="images")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imageName = models.CharField(max_length=30, default=False)
    image = models.ImageField(upload_to=img_path)
    image_ver = models.IntegerField(default=0)
    def __str__(self):
        return '%s' % (self.image)