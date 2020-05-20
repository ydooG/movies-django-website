from django.urls import path

from . import views
app_name = 'discussions'

urlpatterns = [
    path('', views.discussion_list, name='discussion_list'),
    path('discussion/<int:id>', views.DiscussionDetailView.as_view(), name='discussion_details'),
    path('discussion/add_discussion/', views.DiscussionCreateView.as_view(), name='discussion_create'),
    path('discussion/<int:id>/add_theme/', views.ThemeCreateView.as_view(), name='theme_create'),
    path('theme/<int:id>', views.ThemeDetailView.as_view(), name='theme_details'),
    path('theme/<int:id>/add_post/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:id>/add_comment', views.CommentCreateView.as_view(), name='comment_create'),
]
