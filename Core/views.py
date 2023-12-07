from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Core.pre_fun import setip,resize_image,random_string
from Core.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import os
# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    page = 'dashboard'
    portfolio = Project.objects.filter(Status=1)
    blog = Blog.objects.filter(Status=1)
    category = Category.objects.filter(Status=1)

    context = {
        'page':page,
        'portfolio':portfolio,
        'blog':blog,
        'category':category
    }
    return render(request,'Admin/dashboard.html',context)


@login_required
def create_category(request):
    category = Category.objects.last()

    if category:
        reference = f'CATEGORY-0{category.id + 1}' 
    else:
        reference = f'CATEGORY-01'

    page = "category"
    if request.method == 'POST':
        title = request.POST.get('category_title')
        reference = request.POST.get('reference')

        # Create a new Project instance and save it to the database
        new_category = Category(title=title,Reference=reference)
        new_category.save()

        return redirect('category')  # Redirect to a view displaying all projects
    
    context = {
        'page':page,
        'reference': reference,
    }

    return render(request, 'Admin/create-category.html', context)


@login_required
def category_list(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')

        if category_id:
            category = get_object_or_404(Category, id=category_id)
            
            category.Status = 0
            category.save()


    categories = Category.objects.filter(Status=1).order_by('-id')
    page = "category"

    return render(request, 'Admin/category_list.html', {'categories': categories, 'page': page})


@login_required
def edit_category(request,category_id):
    category = Category.objects.get(id=category_id)
    print(category.Reference)
    if request.method == 'POST':
        category.title = request.POST.get('category_title')

        category.save()
        return redirect('category')
    
    context = {
        "category" : category,
    }
    
    return render(request,'Admin/category-edit.html',context)



@login_required
def create_portfolio(request):
    page = "portfolio"
    if request.method == 'POST':
        title = request.POST.get('portfolio_title')
        client_name = request.POST.get('client')
        image_file = request.FILES.get('image')

        # Create a new Project instance and save it to the database
        new_project = Project(title=title, client_name=client_name, image=image_file)
        new_project.save()

        return redirect('portfolio')  # Redirect to a view displaying all projects
    
    context = {
        'page':page
    }

    return render(request, 'Admin/create_project.html', context)



@login_required
def portfolio_list(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')

        if project_id:
            project = get_object_or_404(Project, id=project_id)
            
            # Update the Status field to 0 instead of deleting the entire project
            project.Status = 0
            project.save()

            # Continue with your other deletion logic or redirect as needed
            # ...

    projects = Project.objects.filter(Status=1).order_by('-id')
    page = "portfolio"

    return render(request, 'Admin/portfolio_list.html', {'projects': projects, 'page': page})



@login_required
def view_portfolio(request, portfolio_id):
    page = 'portfolio'
    portfolio = get_object_or_404(Project, id=portfolio_id)
    context = {
        'portfolio': portfolio,
        'page':page
    }
    return render(request, 'Admin/portfolio-view.html', context)


@login_required
def edit_portfolio(request,portfolio_id):
    portfolio = Project.objects.get(id=portfolio_id)
    if request.method == 'POST':
        portfolio.title = request.POST.get('title')
        if len(request.FILES) != 0:
            image = request.FILES['image']
            image_path = resize_image(image,800)
            portfolio.image = image_path
        portfolio.description = request.POST.get('description')

        portfolio.client_name = request.POST.get('client')
        portfolio.save()
        return redirect('portfolio')
    
    context = {
        "portfolio" : portfolio
    }
    
    return render(request,'Admin/portfolio-edit.html',context)


@login_required
def create_blog(request):
    page = "blog"
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        seo_url = request.POST.get('seo_url')
        seo_title = request.POST.get('seo_title')
        seo_description = request.POST.get('seo_description')
        seo_keywords = request.POST.get('seo_keywords')

        new_blog = Blog(
            title=title,
            description=description,
            image=image,
            seo_url=seo_url,
            seo_title=seo_title,
            seo_description=seo_description,
            seo_keywords=seo_keywords
        )
        new_blog.save()

        return redirect('blog')  # Redirect to a view displaying all blogs
    
    context = {
        'page':page
    }

    return render(request, 'Admin/create_blog.html', context)


@login_required
def edit_blog(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        if len(request.FILES) != 0:
            image = request.FILES['image']
            image_path = resize_image(image,800)
            blog.image = image_path
        blog.description = request.POST.get('description')

        url = request.POST.get('seo_url')

        obj = Blog.objects.filter(seo_url=url)

        if obj:
            pass
        else:
           blog.seo_url = request.POST.get('seo_url')

        # blog.Seo_Url = request.POST.get('seo_url')
        blog.seo_title = request.POST.get('seo_title')
        blog.seo_keywords = request.POST.get('seo_keywords')
        blog.seo_description = request.POST.get('seo_description')
        blog.save()
        return redirect('blog')
    
    context = {
        "blog" : blog
    }
    
    return render(request,'Admin/blog-edit.html',context)


@login_required
def delete_portfolio_image(request,portfolio_id):
    portfolio = Project.objects.get(id=portfolio_id)
    portfolio.image.delete()
    return redirect('edit-portfolio' , portfolio_id=portfolio_id)


def blog_list(request):
    blogs = Blog.objects.filter(Status=1).order_by('-id')
    page = "blog"
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=blog_id)
        blog.Status = 0
        blog.save()
        return redirect('blog')
    return render(request, 'Admin/blog_list.html', {'blogs': blogs,'page':page})


@login_required
def view_blog(request, blog_id):
    page = 'blog'
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog,
        'page':page
    }
    return render(request, 'Admin/blog-view.html', context)

@login_required
def delete_blog_image(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.image.delete()
    return redirect('edit-blog' , blog_id=blog_id)
