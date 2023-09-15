from django.shortcuts import render, redirect
from .forms import ChoiceForm, AuthorForm, PostForm, CommentForms
from myapp_sem3 import views
from myapp_sem3.models import Author, Post, Comment


def choice(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            # count = form.cleaned_data['count']
            if game == 'd':
                return views.cube(request)
            elif game == 'r':
                return redirect('rand100') # name
            elif game == 'c':
                return views.coin(request)
    else:
        form = ChoiceForm()
    return render(request, 'myapp_sem4/choice.html', {'form': form})


def author_form(request):
    message = ''
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                biography=form.cleaned_data['biography'],
                birthday=form.cleaned_data['birthday']
            )
            author.save()
            message = 'Автор успешно сохранен'
    else:
        form = AuthorForm()
    return render(request, 'myapp_sem4/base.html', {'form': form, 'message': message, 'title': 'Сохранение автора'})


def post_form(request):
    message = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                category=form.cleaned_data['category'],
                author=form.cleaned_data['author']
            )
            post.save()
            message = 'Пост успешно сохранен'
    else:
        form = PostForm()
    return render(request, 'myapp_sem4/base.html', {'form': form, 'message': message, 'title': 'Сохранение поста'})


def comment_form(request, post_id):
    message = ''
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                comment=form.cleaned_data['comment'],
                post=Post.objects.filter(pk=post_id).first()
            )
            comment.save()
            message = 'Комментарий добавлен'
    else:
        form = CommentForms()
    return render(request, 'myapp_sem4/add_comment.html', {'form': form, 'message': message, 'title': 'Добавление комментария'})
