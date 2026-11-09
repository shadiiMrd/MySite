from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('mystory', views.myStory, name='my_story'),
    path('skill/', views.skill, name='skill'),
    path('education/', views.education, name='education'),
]
