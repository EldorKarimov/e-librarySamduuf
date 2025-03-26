from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from common.models import BaseModel

User = get_user_model()

class Category(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_("slug"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
    
class Tags(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_("slug"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

class News(BaseModel):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_('slug'))
    content = models.TextField(verbose_name=_('content'))
    image = models.ImageField(upload_to='media/news/images', verbose_name=_('image'))
    views = models.PositiveBigIntegerField(default=0, verbose_name=_('views'))
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.CASCADE,
        verbose_name=_('category')
    )
    tags = models.ManyToManyField(Tags, verbose_name=_('tags'))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('user'))

    def __str__(self):
        return self.title