from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
      # IF the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
        # Redirect to Home
            return HttpResponseRedirect('/')
        else:
          # No show Error
            return HttpResponseRedirect(form.errors.as_json())
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):

    posts = Post.objects.get(id=post_id)
    if request.method == "POST":

        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")

    return render(request, 'edit.html', {'posts': posts})


def like(request, post_id):
   
    like = Post.objects.get(id=post_id)
    like.likes += 1
    like.save()
    return HttpResponseRedirect('/')
