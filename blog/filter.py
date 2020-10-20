import django_filters

from .models import *

class PostsFilter(django_filters.FilterSet):
    headline = django_filters.CharFilter(field_name='headline', lookup_expr='icontains', label='')
    class Meta:
        models = Post
        fields = ['headline,']