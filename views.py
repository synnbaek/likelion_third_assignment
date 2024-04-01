from django.shortcuts import render, redirect,get_object_or_404
from .models import Blog
from django.http import HttpResponse

# Create your views here.
def create(request):
    if request.method=='POST' :
        new_blog=Blog()
        new_blog.title=request.POST['title']
        new_blog.content=request.POST['content']
   

        new_blog.save()

        return redirect('detail', new_blog.id)
    return render(request, 'new.html')
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    
    # 세션에서 작성된 값들을 가져옴
    title = request.session.get('new_blog_title', '')
    content = request.session.get('new_blog_content', '')

    # 기존의 블로그 정보와 함께 세션에서 가져온 값들을 합쳐서 전달
    return render(request, 'detail.html', {'blog': blog, 'new_title': title, 'new_content': content})


def list_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'list.html', {'blogs': blogs})


def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')

        # 작성된 값들을 세션에 저장
        request.session['new_blog_title'] = title
        request.session['new_blog_content'] = content

        return redirect('detail')
    else:
        return render(request, 'new.html')