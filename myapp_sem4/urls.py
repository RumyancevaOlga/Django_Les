from django.urls import path
from . import views

urlpatterns = [
    path('choice/', views.choice, name='choice'),
    path('author/', views.author_form, name='author'),
    path('post/', views.post_form, name='post_new'),
    path('add_comment/<int:post_id>/', views.comment_form, name='add_comment'),
]
