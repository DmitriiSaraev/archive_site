from django.contrib import admin

from archive import models


@admin.register(models.Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'type_post', 'title', 'created',
                    'image', 'link']
    prepopulated_fields = {'slug': ('name',)}

