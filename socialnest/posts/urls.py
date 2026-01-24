from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.post_new, name="new-post"),
    path('<int:pk>', views.post_page, name="page"),
    path('<int:pk>/delete/', views.post_delete, name='delete-post'),
    path('<int:pk>/like/', views.post_like, name='like-post'),
]