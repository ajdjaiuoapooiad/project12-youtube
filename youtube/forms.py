from .models import Post,Comment
from django import forms



class YoutubeCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text','thumbnail','movie','category')
        
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','text')