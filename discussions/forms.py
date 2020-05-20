from django import forms
from django.db.models import Q

from accounts.models import CustomUser
from discussions.models import Discussion, Theme, Post, Comment
from movies.models import Movie


class DiscussionCreateForm(forms.ModelForm):
    movie = forms.ModelChoiceField(
        queryset=Movie.objects.filter(Q(discussion=None))
    )

    class Meta:
        model = Discussion
        fields = ('movie', )


class ThemeCreateForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ('title', 'description', 'discussion')


class PostCreateForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.HiddenInput
    )

    theme = forms.ModelChoiceField(
        queryset=Theme.objects.all(),
        widget=forms.HiddenInput
    )

    class Meta:
        model = Post
        fields = ('author', 'text', 'theme')


class CommentCreateForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.HiddenInput
    )

    post = forms.ModelChoiceField(
        queryset=Post.objects.all(),
        widget=forms.HiddenInput
    )

    class Meta:
        model = Comment
        fields = ('author', 'text', 'post')
