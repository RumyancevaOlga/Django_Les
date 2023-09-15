import datetime
from django import forms
from myapp_sem3 import models


class ChoiceForm(forms.Form):
    game = forms.ChoiceField(choices=[('d', 'Кубик'), ('r', 'Случайное число'), ('c', 'Монетка')])
    # count = forms.IntegerField(min_value=1, max_value=64)


class AuthorForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(label='Биография', widget=forms.Textarea)
    birthday = forms.DateField(label='Дата рождения', initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'type': 'date'}))


class PostForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    content = forms.CharField(label='Содержание', widget=forms.Textarea)
    category = forms.CharField(label='Категория', max_length=100)
    author = forms.ModelChoiceField(queryset=models.Author.objects.all())


class CommentForms(forms.Form):
    author = forms.ModelChoiceField(label='Авторы', queryset=models.Author.objects.all())
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)
