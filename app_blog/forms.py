from django import forms
from django.core.exceptions import ValidationError

from app_blog.models import Tag, Post


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('title', 'slug')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'create':
            raise ValidationError('Slug не дожен быть равен "create".')

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Слаг "{new_slug}" уже существует. '
                                  f'Придумайте другой вариант!')
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'text', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'create':
            raise ValidationError('Slug не дожен быть равен "create".')
        return new_slug
