from django.contrib import admin
from .models import Category, Tags, News
from django.utils.translation import gettext_lazy as _

# Admin for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Category

# Admin for Tags model
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Tags

# Admin for News model
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'views', 'created', 'updated')
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags', 'user', 'created')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    readonly_fields = ('views',)

    class Meta:
        model = News

# Register the models with the custom admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(News, NewsAdmin)
