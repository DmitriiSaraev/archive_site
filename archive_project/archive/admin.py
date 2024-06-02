from django.contrib import admin

from archive import models


class ImagePostInLine(admin.TabularInline):
    model = models.ImageForPost
    raw_id_fields = ['post']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'type_post', 'title',
                    'created', 'text_link', 'link']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImagePostInLine]
    list_filter = ['type_post']


@admin.register(models.Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'address', 'boss', 'senior_archivist',
                    'telephone', 'email']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.OperatingMode)
class OpetatingModeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'title', 'number', 'name_day',
                    'start_time_morning', 'end_time_morning',
                    'start_time_lunch', 'end_time_lunch',
                    'text']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'type_link', 'url']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.ListBooks)
class ListBooksAdmin(admin.ModelAdmin):
    list_display = ['numb', 'author', 'name', 'publishing']
    prepopulated_fields = {'slug': ('name',)}










