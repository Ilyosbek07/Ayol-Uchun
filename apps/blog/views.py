from rest_framework import generics

from apps.blog.models import Blog, Category
from apps.blog.serializers import (BlogListSerializer,  # noqa
                                   CategoriesSerializer,
                                   ListBlogWithCategorySerializer)


class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class ListBlogWithCategoryView(generics.ListAPIView):
    serializer_class = ListBlogWithCategorySerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        queryset = Blog.objects.filter(category_id=pk)
        return queryset


class ListBlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get("search", "")
        queryset = Blog.objects.filter(title__icontains=search_query)
        return queryset
