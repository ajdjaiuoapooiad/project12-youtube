from django.urls import path
from . import views

app_name='youtube'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('category/<int:pk>',views.CategoryView.as_view(),name='category'),
    path('create/',views.CreateView.as_view(),name='create'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='detail'),
]