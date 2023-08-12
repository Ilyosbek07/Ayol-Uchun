from django.contrib import admin

from apps.blog.models import Author, Blog, BlogView, Category

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(BlogView)
