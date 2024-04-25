from django.urls import path
from . import views
from .views import profile_detail

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', profile_detail, name='profile_detail'),
    path('photo/<int:photo_id>/comment/', views.add_comment, name='add_comment'),
]
