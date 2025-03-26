from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid4)
    created = models.DateTimeField(auto_now_add = True, verbose_name=_("created"))
    updated = models.DateTimeField(auto_now = True, verbose_name=_("updated"))

    class Meta:
        abstract = True