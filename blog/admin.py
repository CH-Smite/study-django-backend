from django.contrib import admin

from .models import Post, Category

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_field = {"slig": ("name", )}

admin.site.register(Category, CategoryAdmin)