from django.views import generic

from blog.models import Post, Tag


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-date_published')
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context



class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
