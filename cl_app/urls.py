# /categories: A page listing all the categories
# /categories/new: A page with a form to create a new category
# /categories/:category_id: A page to view the detail of a specific category and a list of all of its associated posts
# /categories/:category_id/edit: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here.
# /categories/:category_id/delete: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here.
# /categories/:category_id/posts/new: A page with a form to create a new post, under the current category by default.
# /categories/:category_id/posts/:post_id: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (/categories/:category_id/)
# /categories/:category_id/posts/:post_id/edit: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.
# /categories/:category_id/posts/:post_id/delete: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('new/', views.new_category, name='new_category'),
    path('<int:category_id>/edit', views.edit_category, name='edit_category'),
    path('<int:category_id>/delete', views.delete_category, name='delete_category'),
    path('<int:category_id>/posts', views.post_list, name='post_list'),
    path('<int:category_id>/posts/new', views.new_post, name='new_post'),
    path('<int:category_id>/posts/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('<int:category_id>/posts/<int:post_id>/detail', views.post_detail, name='post_detail'),
    path('<int:category_id>/posts/<int:post_id>/delete', views.delete_post, name='delete_post'),
]