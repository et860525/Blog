from django.contrib import admin

from .models import Post, Tag

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('modified',)


admin.site.register(Tag)