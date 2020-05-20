from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from discussions.forms import DiscussionCreateForm, ThemeCreateForm, PostCreateForm, CommentCreateForm
from discussions.models import Discussion, Theme, Post, Comment


def discussion_list(request):
    if request.method == 'GET':
        context = {}
        context['discussions'] = Discussion.objects.all()
        return render(request, 'discussions/discussion_list.html', context)
    else:
        return HttpResponseNotAllowed(['GET', ])


class DiscussionCreateView(CreateView):
    model = Discussion
    form_class = DiscussionCreateForm
    template_name = 'discussions/discussion_create.html'
    success_url = reverse_lazy('discussions:discussion_list')


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussions/discussion.html'
    context_object_name = 'discussion'

    def get_object(self, queryset=None):
        return get_object_or_404(Discussion, id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_discussion = kwargs['object']
        context['themes'] = curr_discussion.themes.all()
        return context


class ThemeCreateView(CreateView):
    model = Theme
    form_class = ThemeCreateForm
    template_name = 'discussions/theme_create.html'
    success_url = reverse_lazy('discussions:discussion_list')

    def get_initial(self):
        curr_discussion = get_object_or_404(Discussion, id=self.kwargs['id'])
        return {'discussion': curr_discussion}


class ThemeDetailView(DetailView):
    model = Theme
    template_name = 'discussions/theme.html'
    context_object_name = 'theme'

    def get_object(self, queryset=None):
        return get_object_or_404(Theme, id=self.kwargs['id'],)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_theme = kwargs['object']
        context['posts'] = curr_theme.posts.all()
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'discussions/post_create.html'
    success_url = reverse_lazy('discussions:discussion_list')
    form_class = PostCreateForm

    def get_initial(self):
        curr_theme = get_object_or_404(Theme, id=self.kwargs['id'])
        curr_user = self.request.user
        return {'author': curr_user, 'theme': curr_theme}


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'discussions/comment_create.html'
    success_url = reverse_lazy('discussions:discussion_list')
    form_class = CommentCreateForm

    def get_initial(self):
        curr_user = self.request.user
        curr_post = get_object_or_404(Post, id=self.kwargs['id'])
        return {'author': curr_user, 'post': curr_post}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_post = get_object_or_404(Post, id=self.kwargs['id'])
        context['post'] = curr_post
        return context


