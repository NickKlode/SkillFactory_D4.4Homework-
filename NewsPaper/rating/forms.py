from django.forms import ModelForm, BooleanField 
from .models import *


class PostForm(ModelForm):
    check_box = BooleanField(label='Галочка!!!') 

    class Meta:
        model = Post
        fields = [
            'author',
            'categoryType',
            'postCategory',
            'title',
            'text',
            'check_box',
        ]