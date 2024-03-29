from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_as = True

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
