from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .form import PostForm
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #request.POST가 입력했던 데이터를 가지고있음 안넣을 시 폼을 제출할 때 데이터가 없어짐
        if form.is_valid(): #데이터의 유효성 검사
            post = form.save(commit=False) #commit=False => 넘겨진 데이터를 바로 Post모델에 저장하지 말라는 의미
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) #pk가 없을경우 404
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) #instance=post => 수정완료를 눌렀을 때 이전에 입력한 값들이 유지된다.
        if form.is_valid():
            post = form.save(commit=False)
            post.User = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)  #form을 새로 요청 할 때 이전의 값들이 유지 된다.
    return render(request, 'blog/post_edit.html', {'form': form})