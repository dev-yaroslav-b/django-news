from django.contrib import admin

from .models import Post


def approve_posts(modeladmin, request, queryset):
    queryset.update(approved=True)
    approve_posts.short_description = "Approve selected"


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'approved']
    list_filter = ['text', 'approved']
    actions = [approve_posts]


admin.site.register(Post, PostAdmin)
