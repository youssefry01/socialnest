from django import forms 
from . import models 

class CreatePost(forms.ModelForm): 
    class Meta: 
        model = models.Post
        fields = ['title','body','banner']
   
        labels = {
            'title': 'Post Title',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Ex: My First Post'}),
        }