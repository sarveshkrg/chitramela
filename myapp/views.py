from django.shortcuts import render
from . models import Post
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# this is function based view - user defined
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    return render(request, 'myapp/about.html')

# this is class based view - build in (work as above index method)
class PostListView(ListView):
    model = Post
    template_name = 'myapp/index.html' # <app-name>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False