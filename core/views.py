from django.shortcuts import render
from .models  import Core
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,UpdateView,DeleteView



class IndexView(ListView):
    
    model= Core
    template_name= 'core/index.html'
    context_object_name = 'index'

class SingleView(DetailView):

    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'

class ProfileView(ListView):
    model = User
    template_name = 'core/user_profile.html'
    context_object_name = 'user'

class AboutView (ListView):

    model = Core
    template_name = 'core/about.html'
 