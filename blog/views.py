from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone

from .models import Post


def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_posts': latest_posts}

    return render(
        request,
        template_name='blog/index.html',
        context=context
    )


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(
        request,
        template_name='blog/detail.html',
        context={'post': post}
    )


def create(request):
    return render(
        request,
        template_name='blog/create.html',
    )


def post(request):
    post = Post(
        title=request.POST['post_title'],
        body=request.POST['post_body'],
        pub_date=timezone.now()
    )
    post.save()

    return HttpResponseRedirect('/')

