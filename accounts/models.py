from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    first_name = models.CharField(max_length=50, verbose_name=_("first name"))
    last_name = models.CharField(max_length=50, verbose_name=_("last name"))
    patronymic = models.CharField(max_length=50, verbose_name=_("patronymic"))
    email = models.EmailField(verbose_name=_("email"))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
class Faculty(BaseModel):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("name"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("faculty")
        verbose_name_plural = _("faculties")

class Group(BaseModel):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("name"))
    faculty = models.ForeignKey(
        Faculty,
        related_name="faculty",
        on_delete=models.CASCADE,
        verbose_name=_("faculty")
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")
    
class Student(BaseModel):
    class StudentTypeChoices(models.TextChoices):
        BACHELOR = 'BA', _('Bachelor')
        MASTER = 'MA', _('Master')
        DOCTORATE = 'PHD', _('Doctorate')

    class StudentEnrollmentChoices(models.TextChoices):
        FULL_TIME = 'FT', _('Full time')
        PART_TIME = 'PT', _('Part time')
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("user"))
    phone = models.CharField(max_length=13, verbose_name=_("phone"))
    group = models.ForeignKey(
        Group,
        related_name="group",
        on_delete=models.CASCADE,
        verbose_name=_("group")
    )

    student_type = models.CharField(
        max_length=3,
        choices=StudentTypeChoices.choices,
        default=StudentTypeChoices.BACHELOR,
        verbose_name=_("student type")
    )
    
    student_enrollment = models.CharField(
        max_length=2,
        choices=StudentEnrollmentChoices.choices,
        default=StudentEnrollmentChoices.FULL_TIME,
        verbose_name=_("student enrollment")
    )

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")