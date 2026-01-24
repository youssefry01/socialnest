from django import forms
from .models import Post


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': "What's on your mind?",
                'rows': 6,
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all resize-none'
            }),
        }
