from django.urls import path

from apps.blog.views import (CategoriesView, ListBlogView,
                             ListBlogWithCategoryView)

urlpatterns = [
    path("category/", CategoriesView.as_view(), name="category"),
    path("category/<int:pk>/", ListBlogWithCategoryView.as_view(), name="category-blog"),
    path("", ListBlogView.as_view(), name="blog-list"),
]
