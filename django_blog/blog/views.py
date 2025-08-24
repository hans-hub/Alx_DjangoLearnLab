from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# List all posts - public
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"   # blog/templates/blog/post_list.html
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 10

# Show single post - public
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"  # blog/templates/blog/post_detail.html
    context_object_name = "post"

# Create a post - only authenticated users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post-list")
    # Redirect to login if not authenticated
    login_url = "/login/"

    def form_valid(self, form):
        # Set the author to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post - only the author can edit
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post - only the author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

