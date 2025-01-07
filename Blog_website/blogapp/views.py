from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.http import HttpResponse

def create_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blogapp/createblog/')  # Redirect to a success page or another view
    else:
        form = PostForm()
    return render(request, 'blogapp/Create_Blog.html', {'form': form})


# views.py


def home(request):
    posts = Post.objects.order_by('-date_posted')[:3]
    return render(request, 'blogapp/Home.html', {'posts': posts})


def all_blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/All_Blogs.html', {'posts': posts})

def blog_detail(request,slug):
    posts = Post.objects.get(slug=slug)
    return render(request,'blogapp/Blog_Detail.html',{'post':posts})
