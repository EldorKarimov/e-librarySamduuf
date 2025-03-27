from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

from common.models import BaseModel

User = get_user_model()


class BookCategory(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_("slug"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Book category")
        verbose_name_plural = _("Book categories")
    
class BookLang(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Book language")
        verbose_name_plural = _("Book languages")

class Publication(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("publication")
        verbose_name_plural = _("publications")
    


class EBook(BaseModel):
    class BookWritingChoices(models.TextChoices):
        KRILL = 'KR', _("Krill")
        LATIN = 'LT', _("Latin")

    name = models.CharField(max_length=80, verbose_name=_("name"))
    slug = models.SlugField(max_length=80, unique=True, verbose_name=_("slug"))
    views = models.PositiveBigIntegerField(default=0, verbose_name=_("views"), help_text="views for book")
    downloads = models.PositiveBigIntegerField(default=0, verbose_name=_("downloads"))
    writing = models.CharField(
        max_length=2,
        choices=BookWritingChoices.choices,
        verbose_name=_('writing')
    )
    num_of_pages = models.PositiveIntegerField(verbose_name=_("number of pages"))
    year_of_pub = models.PositiveIntegerField(verbose_name=_("year of published"))
    
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(upload_to='media/book/images', verbose_name=_('image'))
    qr = models.ImageField(upload_to='media/qr/images', verbose_name=_("QR code"))
    file = models.FileField(
        upload_to='media/book/files',
        verbose_name=_("file"),
        validators=[FileExtensionValidator(allowed_extensions=('pdf',))]
    )
    

    lang = models.ForeignKey(
        BookLang,
        on_delete=models.SET_NULL, null=True,
        related_name='book_languages',
        verbose_name=_("language")
    )
    publication = models.ForeignKey(
        Publication,
        on_delete=models.SET, null=True,
        related_name='publication',
        verbose_name=_('publication')
    )
    category = models.ForeignKey(
        BookCategory,
        on_delete=models.CASCADE,
        related_name='category',
        verbose_name=_('category')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, null=True,
        verbose_name=_('user')
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "EBook"
        verbose_name_plural = "EBooks"