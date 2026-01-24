from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, UserForm, PasswordChangeForm, UserRegistrationForm

# Create your views here.
def register_view(request):
    if request.method == "POST": 
        form = UserRegistrationForm(request.POST) 
        if form.is_valid(): 
            user = form.save()
            # Create a profile for the new user
            Profile.objects.create(user=user)
            login(request, user)
            return redirect("posts:list")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", { "form": form })

def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })

def logout_view(request):
    if request.method == "POST": 
        logout(request) 
        return redirect("posts:list")


def profile_view(request, username):
    """View a user's profile"""
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    user_posts = user.post_set.all().order_by('-date')
    
    # Check if current user is following this user
    is_following = False
    if request.user.is_authenticated:
        is_following = request.user.profile.following.filter(user=user).exists()
    
    # Count followers (profiles that follow this user) and following (profiles this user follows)
    follower_count = Profile.objects.filter(following=profile).count()
    following_count = profile.following.count()
    
    context = {
        'profile_user': user,
        'profile': profile,
        'user_posts': user_posts,
        'post_count': user_posts.count(),
        'is_following': is_following,
        'follower_count': follower_count,
        'following_count': following_count,
    }
    return render(request, 'users/view_profile.html', context)


@login_required(login_url='users:login')
def edit_profile_view(request):
    """Edit your own profile"""
    profile = request.user.profile
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        password_form = PasswordChangeForm(request.user, request.POST)
        
        # Check if password change was submitted (if any password field has data)
        password_changed = False
        password_fields_filled = any([
            request.POST.get('old_password'),
            request.POST.get('new_password1'),
            request.POST.get('new_password2')
        ])
        
        if password_fields_filled:
            if password_form.is_valid():
                password_form.save()
                password_changed = True
                # Update session to prevent logout after password change
                update_session_auth_hash(request, request.user)
        
        # Handle profile updates
        profile_valid = user_form.is_valid() and profile_form.is_valid()
        password_valid = not password_fields_filled or password_form.is_valid()
        
        if profile_valid and password_valid:
            user_form.save()
            profile_form.save()
            return redirect('users:profile', username=request.user.username)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        password_form = PasswordChangeForm(request.user)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
    }
    return render(request, 'users/edit_profile.html', context)


@login_required(login_url='users:login')
def follow_user(request, username):
    """Follow a user"""
    user_to_follow = get_object_or_404(User, username=username)
    
    if user_to_follow == request.user:
        return redirect('users:profile', username=username)
    
    request.user.profile.following.add(user_to_follow.profile)
    return redirect('users:profile', username=username)


@login_required(login_url='users:login')
def unfollow_user(request, username):
    """Unfollow a user"""
    user_to_unfollow = get_object_or_404(User, username=username)
    
    if user_to_unfollow == request.user:
        return redirect('users:profile', username=username)
    
    request.user.profile.following.remove(user_to_unfollow.profile)
    return redirect('users:profile', username=username)