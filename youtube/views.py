from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from .forms import YoutubeCreateForm

class IndexView(generic.ListView):
    model=Post
    
class CreateView(generic.CreateView):
    model=Post
    form_class=YoutubeCreateForm
    success_url=reverse_lazy('youtube:index')
    
    def __str__(self):
        return self.title
    
class DetailView(generic.DetailView):
    model=Post
    