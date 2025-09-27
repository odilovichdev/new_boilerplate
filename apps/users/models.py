from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.common.models import BaseModel
from apps.users.managers import UserManager


class Users(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_("Email"), unique=True)
    phonenumber = PhoneNumberField(_("Phone Number"), unique=True)
    fullname = models.CharField(_("Fullname"), null=True, blank=True)
    birth_date = models.DateTimeField(_("Birth Date"), null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to='users/', null=True, blank=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_superuser = models.BooleanField(_("Is Superuser"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    manager = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.email}"
