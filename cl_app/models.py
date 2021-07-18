from django.db.models.deletion import CASCADE
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=128)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_created}: {self.category_name}"

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='posts')
    post_title = models.CharField(max_length=128)
    post_content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.post_title}"
    