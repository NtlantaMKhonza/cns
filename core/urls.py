from django.urls import path 
from . import views


app_name ='core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<slug:slug>/', views.SingleView.as_view(), name='singles'),
    
]