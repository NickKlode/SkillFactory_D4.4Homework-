from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'dateCreation': ['gte'],
            'author__authorUser__first_name': ['exact'],
        }