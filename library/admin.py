from django.contrib import admin
from .models import BookCategory, BookLang, Publication, EBook
from django.utils.translation import gettext_lazy as _


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(BookLang)
class BookLangAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(EBook)
class EBookAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'writing', 'num_of_pages', 'year_of_pub', 
        'lang', 'publication', 'category', 'user'
    )
    search_fields = (
        'name', 'lang__name', 'publication__name', 
        'category__name', 'user__username'
    )
    list_filter = (
        'writing', 'lang', 'publication', 'category', 'user'
    )
    ordering = ('name',)
    list_per_page = 20
    readonly_fields = ('views', 'downloads')  # Prevent editing of views and downloads
    prepopulated_fields = {'slug':('name', )}

    fieldsets = (
        (_('General Information'), {
            'fields': ('name', 'slug', 'name_uz', 'name_en', 'name_ru', 'writing', 'num_of_pages', 'year_of_pub', 'description', 'description_uz', 'description_en', 'description_ru')
        }),
        (_('Media'), {
            'fields': ('image', 'file', 'qr')
        }),
        (_('Relationships'), {
            'fields': ('lang', 'publication', 'category', 'user')
        }),
        (_('Statistics'), {
            'fields': ('views', 'downloads')
        }),
    )