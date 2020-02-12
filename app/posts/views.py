from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import generic

from .forms import PostForm
from .models import Post


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(approved=True).order_by('text')


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if request.user.is_superuser:
                post.approved = True
            post.save()
            return redirect('/')
    else:
        form = PostForm()

    template = 'pages/create_post.html'
    forms = {
        'form': form
    }
    return render(request, template, forms)
