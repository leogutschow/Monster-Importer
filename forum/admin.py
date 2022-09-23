from django.contrib import admin
from .models import Forum, Category


# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'created_at', 'published'
    )
    list_editable = ('published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Forum, ForumAdmin)
admin.site.register(Category, CategoryAdmin)

