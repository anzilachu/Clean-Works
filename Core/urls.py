from django.urls import path
from Core.views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),

    path('add-category/',create_category,name='add-category'),
    path('category/',category_list,name='category'),
    path('edit-category/<int:category_id>/',edit_category,name='edit-category'),

    path('add-portfolio/',create_portfolio,name='add-portfolio'),
    path('portfolio/',portfolio_list,name='portfolio'),
    path('view-portfolio/<int:portfolio_id>/',view_portfolio,name='view-portfolio'),
    path('edit-portfolio/<int:portfolio_id>/',edit_portfolio,name='edit-portfolio'),
    path('delete-portfolio-image/<int:portfolio_id>/',delete_portfolio_image,name='delete-portfolio-image'),


    path('add-blog/',create_blog,name='add-blog'),
    path('blog/', blog_list,name='blog'),
    path('edit-blog/<int:blog_id>/',edit_blog,name='edit-blog'),
    path('view-blog/<int:blog_id>/',view_blog,name='view-blog'),
    path('delete-blog-image/<int:blog_id>/',delete_blog_image,name='delete-blog-image'),
]