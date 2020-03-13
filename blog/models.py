from django.conf import settings
from django.db import models
from django.utils import timezone

#models-> Post가 장고 모델임을 의미
#models때문에 장고는 Post가 데이터베이스에 저장되어야한다고 인식
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #ForeignKey -> 다른 모델에 대한 링크
    title = models.CharField(max_length=200) #CharField -> 글자 수가 제한된 텍스트를 정의할 때 사용
    text = models.TextField() #TextField -> 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    #작성일
    created_date = models.DateTimeField(default=timezone.now) #DateTimeField -> 날짜와 시간을 의미
    #게시일
    published_date = models.DateTimeField(blank=True, null=True) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title