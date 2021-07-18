from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_content']