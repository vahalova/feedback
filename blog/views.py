from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context
from django.http import Http404
import os
nazev_kurzu = os.environ.get('nazev_kurzu', 'ke kurzu')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'things/post_list.html', {'posts': posts, 'nazev_kurzu': nazev_kurzu})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if post.published_date<=timezone.now():
        return render(request, 'things/post_detail.html', {'post': post, 'nazev_kurzu': nazev_kurzu})
    else:
        raise Http404

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'things/post_edit.html', {'form': form, 'nazev_kurzu': nazev_kurzu})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'things/post_edit.html', {'form': form, 'nazev_kurzu': nazev_kurzu})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'things/add_comment_to_post.html', {'form': form, 'nazev_kurzu': nazev_kurzu})
