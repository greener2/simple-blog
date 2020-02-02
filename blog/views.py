from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from blog.models import Post, Tag


def index(request):
    tags = Tag.objects.all()
    if request.method == "GET":
        search_query = request.GET.get("search_box", None)
        print(search_query)
        if not search_query:
            template = "blog/index.html"
            posts = Post.objects.all().order_by('-date_published')
        else:
            template = "blog/search_result.html"
            posts = Post.objects.filter(Q(title__icontains=search_query) | Q(subtitle__contains=search_query) | Q(body__contains=search_query)).order_by('-date_published')
    else:
        search_query = ""
        template = "blog/index.html"
        posts = Post.objects.all().order_by('-date_published')

    return render(request, template, {"posts": posts, "tags": tags, "search_query": search_query})


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


def tag_search(request, name):
    posts = Post.objects.filter(tags__name=name)
    all_tags = Tag.objects.all()

    return render(request, "blog/tag-search.html", context={"posts": posts, "tag_name": name, "tags": all_tags})