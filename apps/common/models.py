from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    class Meta:
        abstract = True


class Contact(BaseModel):
    message = models.TextField(_("Message"))
    full_name = models.CharField(_("Fullname"), max_length=255)
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    document = models.FileField(_("Ducument"), upload_to='documents/')

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return f"{self.full_name}"


class CompanyProfile(BaseModel):
    longitude = models.FloatField(_("Longitude"), default=0.0)
    latitude = models.FloatField(_("Latitude"), default=0.0)
    email = models.EmailField(_("Email"))
    landmark = models.CharField(_("Landmark"), max_length=255)
    work_time = models.CharField(_("Work Time"), max_length=100)
    phone_number = models.CharField(_("Phone Number"), max_length=20)

    class Meta:
        verbose_name = _("Company Profile")
        verbose_name_plural = _("Company Profiles")

    def __str__(self):
        return f"{self.email}"



class CompanySocialMedia(BaseModel):
    link = models.URLField(_("Link"))
    title = models.CharField(_("Title"), max_length=100)
    icon_key = models.CharField(_("Icon Key"), max_length=100)

    class Meta:
        verbose_name = _("Company Social Media")
        verbose_name_plural = _("Company Social Medias")

    def __str__(self):
        return f"{self.title}"



