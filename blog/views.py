from django.shortcuts import render
from django.views import generic
from blog.models import Post


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-date_published')
    template_name = "blog/index.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post-detail.html"

# def index(request):
#     posts = Post.objects.all()
#     return render(request, "blog/index.html", context={"posts": posts})
