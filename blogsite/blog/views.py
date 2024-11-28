from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, "new_post.html", {'form': form})

def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.order_by("-created_on")
    new_comment = None
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return render(request, "add_comment.html")
    else:
        form = CommentForm()
    return render(request, "add_comment.html", {'form': form, 'post': post, 'comments': comments, 'new_comment': new_comment})

def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, 'delete.html', {'post': post})

def sign_up_by_html(request):
    info = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
    return render(request, 'reg_page.html', info)

def main_page(request):
    return HttpResponse("Это главная страница")


