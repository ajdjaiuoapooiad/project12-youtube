from django.urls import path
from . import views

app_name='youtube'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('create/',views.CreateView.as_view(),name='create'),
]