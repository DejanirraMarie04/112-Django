from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class PostListView(ListView):  # GET Request -> List
    # template_name is the attribute to render the html
    template_name = "posts/list.html"
    # model attribute let django know from which model (table) we want to retrieve data
    model = Post
    # context_object_name attribute allow us to change the 
    # variable on how we call it inside of templates
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(LoginRequiredMixin, DetailView): # GET Request -> Single element (Object)
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(LoginRequiredMixin, CreateView): # POST Request -> empty form (HTML)
    template_name = "posts/new.html"
    model = Post
    # fields attribute is a list that allow us to enable/disable the inputs to render in the html
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # POST Request -> filled form (HTML)
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # POST Request 
    template_name = "posts/delete.html"
    model = Post
    # success_url attribute allow us to redirect the user if the request was successful
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False