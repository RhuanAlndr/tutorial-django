from django.views.generic import DetailView, ListView
from .models import Post

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

# vou fazer funções e hoje é classes, preciso aprender as duas
