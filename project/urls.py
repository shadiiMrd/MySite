from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.list, name='list'),
    path('detail/<int:project_id>/', views.detail, name='detail'),
]