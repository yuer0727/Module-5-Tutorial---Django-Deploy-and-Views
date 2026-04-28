from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # 获取并按时间排序文章
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 将 posts 字典传递给模板
    return render(request, 'blog/post_list.html', {'posts': posts})