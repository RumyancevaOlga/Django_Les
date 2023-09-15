from django.contrib import admin
from myapp_sem3.models import Author, Post, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name']
    fields = ['name', 'surname', 'email', 'biography', 'birthday']
    readonly_fields = ['name', 'surname', 'birthday']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author']
    ordering = ['title']
    fields = ['title', 'content', 'author', 'public_date']
    readonly_fields = ['title', 'author', 'public_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'comment']
    ordering = ['author']
    fields = ['author', 'comment', 'public_date', 'change_date']
    readonly_fields = ['author', 'public_date', 'change_date']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
