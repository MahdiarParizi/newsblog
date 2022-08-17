from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request ) :
    post = Post.objects.filter(status = 'p')
    context = {
        'post': post,

    }
    return render(request,'blog/index.html', context)

def detail(request,slug):
    detail = get_object_or_404(Post , slug=slug , status= 'p')
    context = {
        'detail':detail
    }
    return render(request , 'blog/post.html' , context)


def contact(request):
    return render(request , 'blog/contact.html')

def about(request):
    return render(request , 'blog/about.html')

#def post(request):
    #return render(request , 'blog/post.html')
