from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, PostImage
from django.contrib.auth.decorators import login_required
from . import forms 

# Create your views here.
def posts_list(request):
    all_posts = Post.objects.all().order_by('-date')
    following_posts = None
    
    # If user is authenticated, get posts from people they follow
    if request.user.is_authenticated:
        following_profiles = request.user.profile.following.all()
        following_users = [profile.user for profile in following_profiles]
        following_posts = Post.objects.filter(author__in=following_users).order_by('-date')
    
    context = {
        'all_posts': all_posts,
        'following_posts': following_posts,
        'user_is_authenticated': request.user.is_authenticated,
    }
    return render(request, 'posts/posts_list.html', context)

def post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST': 
        form = forms.CreatePost(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
            
            # Handle multiple image uploads
            images = request.FILES.getlist('images')
            for image in images:
                PostImage.objects.create(post=newpost, image=image)
            
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })

@login_required
def post_delete(request, pk):
    post = Post.objects.get(id=pk, author=request.user)
    post.delete()
    return redirect('posts:list')

@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    # Redirect back to the referrer (previous page) or default to home
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    return redirect('posts:list')
    