from .models import Post
from django import forms



class YoutubeCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text','thumbnail','movie')