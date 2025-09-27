from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class BookLanguage(BaseModel):
    language = models.CharField(_("Language"), max_length=250, unique=True)

    class Meta:
        verbose_name = _("Book Language")
        verbose_name_plural = _("Book Languages")

    def __str__(self):
        return f"{self.language}"


class BookCategory(BaseModel):
    title = models.CharField(_("Title"), max_length=250, unique=True)
    order = models.PositiveIntegerField(_("Order"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.title}"


class Book(BaseModel):
    class DiscountType(models.TextChoices):
        PERCENTAGE = "PERCENTAGE", _("Percentage")
        FIXED = "FIXED", _("FIXED")

    class Level(models.TextChoices):
        BEGINNER = "BEGINNER", _("Beginner")
        MIDDLE = "MIDDLE", _("Middle")
        ADVANCED = "ADVANCED", _("Advanced")

    title = models.CharField(_("Title"), max_length=250)
    owner_name = models.CharField(_("Owner Name"), max_length=250)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    discount_type = models.CharField(_("Discount Type"), max_length=20, choices=DiscountType.choices)
    discount_value = models.DecimalField(_("Discount Value"), max_digits=10, decimal_places=2)
    level = models.CharField(_("Level"), max_length=20, choices=Level.choices)
    image = models.ImageField(_("Image"), upload_to="books/", null=True, blank=True)
    rating = models.FloatField(_("Rating"), default=0)
    desc = models.TextField(_("Description"), null=True, blank=True)
    page_count = models.SmallIntegerField(_("Page Count"))
    publish_date = models.DateField(_("Publish Date"))

    category = models.ForeignKey("BookCategory", on_delete=models.CASCADE, related_name="books")
    language = models.ForeignKey("BookLanguage", on_delete=models.CASCADE, related_name="languages")

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return f"{self.title}"
