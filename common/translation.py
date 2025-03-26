from modeltranslation.translator import TranslationOptions, register

from news.models import *
from library.models import *

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Tags)
class TagsTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

# =============== For books =======================

@register(BookCategory)
class BookCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(BookLang)
class BookLangTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(EBook)
class EBookTranslationOptions(TranslationOptions):
    fields = ('name', 'description')