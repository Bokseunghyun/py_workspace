from django.contrib import admin
from .models import Post

#관리자 페이지
#모델링 한 글들을 장고 관리자에서 추가,수정,삭제 가능
admin.site.register(Post) #Post 모델 등록