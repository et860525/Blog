import django_filters
from django import forms

from .models import *

class PostsFilter(django_filters.FilterSet):
    headline = django_filters.CharFilter(field_name='headline', lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'Enter headline'}))
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple(),
    )
    class Meta:
        models = Post
        fields = ['headline', 'tags',]