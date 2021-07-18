from cl_app.models import Category, Post
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from .forms import CategoryForm, PostForm

def get_category(category_id):
    try:
	    return Category.objects.get(id=category_id)
    except:
        return HttpResponse(f"A category with id {category_id} doesn't exist")

def category_list(request):
    data = {
        'categories': Category.objects.all()
    }
    return render(request, 'categories/home.html', data)

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form, 'type_of_request': 'New'})

def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, {'category': category}, instance=category)
        if form.is_valid():
            print("form is valid")
            category = form.save(commit=False)
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_category(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":      
        print('deleting category!!!!')
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_delete.html', {'category': category})

def get_post(post_id):
    try:
	    return Post.objects.get(id=post_id)
    except:
        return HttpResponse(f"A post with id {post_id} doesn't exist")

def post_list(request, category_id):
    category = get_category(category_id)
    posts = category.posts.all()
    return render(request, 'posts/post_list.html', {'category': category, 'posts': posts})

def post_detail(request, category_id, post_id):
    category= get_category(category_id)
    post = get_post(post_id)
    return render(request, 'posts/post_detail.html', {'category': category, 'post': post})

def new_post(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_list', category_id=category.id)
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form, 'type_of_request': 'New', 'category': category})

def edit_post(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            return redirect('post_list', category_id = category.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'type_of_request': 'Edit', 'category': category})

def delete_post(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    if request.method == "POST":      
        post.delete()
        return redirect('post_list', category_id = category.id)
    return render(request, 'posts/post_delete.html', {'category': category, 'post': post})
