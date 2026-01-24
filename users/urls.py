from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"), # type: ignore
    path('profile/edit/', views.edit_profile_view, name="edit-profile"),  # Must come before profile/<username>/
    path('profile/<str:username>/', views.profile_view, name="profile"),
    path('<str:username>/follow/', views.follow_user, name="follow"),
    path('<str:username>/unfollow/', views.unfollow_user, name="unfollow"),
]