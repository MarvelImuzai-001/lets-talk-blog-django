# from django.shortcuts import render, redirect, get_object_or_404
# from blogs.models import Category, Blog
# from django.contrib.auth.decorators import login_required, user_passes_test
# from .forms import CategoryForm, BlogPostForm, AddUserForm, EditUserForm
# from blogs.models import Blog
# from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User
# from django.contrib import auth

# # Create your views here.
# @login_required(login_url="login")
# def dashboard(request):
#     category_count = Category.objects.all().count()
#     blogs_count = Blog.objects.all().count()
    
#     context = {
#         "category_count" : category_count,
#         "blogs_count" : blogs_count,
#     }
    
#     return render(request,"dashboard/dashboard.html", context)


# def categories(request):
#     return render(request, "dashboard/categories.html")

# def add_category(request):
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("categories")
#     form = CategoryForm()
#     context = {
#       "form" : form,  
#     }
#     return render(request, "dashboard/add_category.html", context)

# def edit_category(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     if request.method == "POST":
#         form = CategoryForm(request.POST, instance=category )
#         if form.is_valid():
#             form.save()
#             return redirect("categories")
            
#     form = CategoryForm(instance=category)
#     context = {
#         "form" : form,
#         "category" : category
#     }
#     return render(request, "dashboard/edit_category.html", context)

# def delete_category(request,pk):
#     category = get_object_or_404(Category, pk=pk)
#     category.delete()
#     return redirect("categories")

# def posts(request):
#     posts = Blog.objects.all()
#     context = {
#         "posts" : posts
#     }
#     return render(request, "dashboard/posts.html", context)

# def add_posts(request):
#     if request.method == "POST":
#         form = BlogPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user 
#             post.save()
#             title = form.cleaned_data["title"]
#             post.slug = slugify(title) + "-" + str(post.id)
#             post.save()
#             return redirect("posts")
#     form = BlogPostForm()
#     context = {
#         "form" : form,
#     }
#     return render(request, "dashboard/add_posts.html", context)

# def edit_posts(request, pk):
#     post = get_object_or_404(Blog, pk=pk)
#     if request.method == "POST":
#         form = BlogPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             title = form.cleaned_data["title"]
#             post.slug = slugify(title) + "-" + str(post.id)
#             post.save()
#             return redirect("posts")
#     form = BlogPostForm(instance=post)
#     context = {
#         "form" : form,
#         "post" : post,
#     }
#     return render(request, "dashboard/edit_posts.html", context)

# def delete_posts(request, pk):
#     post = get_object_or_404(Blog,pk=pk)
#     post.delete()
#     return redirect("posts")

# def users(request):
#     users = User.objects.all()
#     context = {
#         "users" : users,
#     }
#     return render(request, "dashboard/users.html", context)

# def add_users(request):
#     if request.method == "POST":
#         form = AddUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("users")
#     form = AddUserForm()
#     context = {
#         "form" : form,
#     }
#     return render(request, "dashboard/add_users.html", context)

# def edit_users(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == "POST":
#         form = EditUserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect("users")     
#     form = EditUserForm(instance=user)
#     context = {
#         "form" : form,
#     }
#     return render(request, "dashboard/edit_users.html",context)

# def delete_users(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     user.delete()
#     return redirect("users")

# # def logout(request):
# #     auth.logout(request)
# #     return redirect("home")

from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CategoryForm, BlogPostForm, AddUserForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib import auth

# Helper function to check if the user is staff or superuser
def is_staff_or_superuser(user):
    return user.is_staff or user.is_superuser

# Apply the decorator to ensure the user is logged in and is staff or superuser
@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    
    context = {
        "category_count": category_count,
        "blogs_count": blogs_count,
    }
    
    return render(request, "dashboard/dashboard.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def categories(request):
    return render(request, "dashboard/categories.html")

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm()
    context = {
        "form": form,  
    }
    return render(request, "dashboard/add_category.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
            
    form = CategoryForm(instance=category)
    context = {
        "form": form,
        "category": category
    }
    return render(request, "dashboard/edit_category.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("categories")

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def posts(request):
    posts = Blog.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "dashboard/posts.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def add_posts(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            title = form.cleaned_data["title"]
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect("posts")
    form = BlogPostForm()
    context = {
        "form": form,
    }
    return render(request, "dashboard/add_posts.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def edit_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data["title"]
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect("posts")
    form = BlogPostForm(instance=post)
    context = {
        "form": form,
        "post": post,
    }
    return render(request, "dashboard/edit_posts.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def delete_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect("posts")

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def users(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "dashboard/users.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def add_users(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    form = AddUserForm()
    context = {
        "form": form,
    }
    return render(request, "dashboard/add_users.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def edit_users(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users")     
    form = EditUserForm(instance=user)
    context = {
        "form": form,
    }
    return render(request, "dashboard/edit_users.html", context)

@login_required(login_url="login")
@user_passes_test(is_staff_or_superuser, login_url='home')
def delete_users(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("users")

# Uncomment and use if needed
# @login_required(login_url="login")
# def logout(request):
#     auth.logout(request)
#     return redirect("home")
