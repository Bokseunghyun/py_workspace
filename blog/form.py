from django import forms

from .models import Post

#forms.ModelForm으로 장고에 이 폼이 모델폼이라는것을 인식하도록 함
class PostForm(forms.ModelForm):
    class Meta: #폼을 만들기 위해 어떤 모델이 사용될 것인지 장고에 알려줌
        model = Post
        fields = ('title', 'text') #제목과 내용만 보이게