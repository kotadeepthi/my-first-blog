from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog1/post_list.html', {'posts':posts})
def post_detail(request,pk):
   # post=Post.objects.get(pk=pk)
    post=get_object_or_404(Post,pk=pk)    
    return render(request,'blog1/post_detail.html',{'post':post})
