from django import forms
from django.core.exceptions import ValidationError

from app_blog.models import Tag


class TagForm(forms.Form):
    title = forms.CharField(label='Название тега', max_length=55)
    slug = forms.SlugField(label='Слаг тега', max_length=55)

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})


    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'create':
            raise ValidationError('Slug не дожен быть равен "create".')
        return new_slug

    def save(self):
        new_tag = Tag.objects.create(
            title=self.cleaned_data.get('title'),
            slug=self.cleaned_data.get('slug'),
        )
        return new_tag
