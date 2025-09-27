from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class CourseLanguage(BaseModel):
    language = models.CharField(_("Language"),max_length=50, unique=True)

    class Meta:
        verbose_name = _("Course Language")
        verbose_name_plural = _("Course Languages")

    def __str__(self):
        return f"{self.language}"

class CourseCategory(BaseModel):
    order = models.IntegerField(_("Order"))
    title = models.CharField(_("Title"), max_length=100)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.title}"

class Course(BaseModel):

    class DiscountType(models.TextChoices):
        PERCENTAGE = 'PERCENTAGE', _("PERCENTAGE")
        FIXED = 'FIXED', _("FIXED")

    class CourseLevel(models.TextChoices):
        BEGINNER = 'BEGINNER', _("BEGINNER")
        MIDDLE = 'MIDDLE', _("MIDDLE")
        ADVANCED = 'ADVANCED', _("ADVANCED")

    title = models.CharField(_("Title"), max_length=200)
    owner_name = models.CharField(_("Owner Name"), max_length=200)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    discount_type = models.CharField(_("Discount Type"), max_length=20, choices=DiscountType.choices)
    discount_value = models.DecimalField(_("Discount Value"), max_digits=10, decimal_places=2)
    level = models.CharField(_("Level"), max_length=10, choices=CourseLevel.choices)
    image = models.ImageField(_("Image"), upload_to='courses/')
    rating = models.FloatField(_("Rating"))

    category = models.ForeignKey("CourseCategory", on_delete=models.CASCADE, related_name="courses")
    language = models.ForeignKey("CourseLanguage", on_delete=models.CASCADE, related_name="courses")


    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return f"{self.title}"

class Module(BaseModel):
    title = models.CharField(_("Title"), max_length=200)
    order = models.IntegerField(_("Order"))

    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Module")
        verbose_name_plural = _("Modules")

    def __str__(self):
        return f"{self.title}"

class Video(BaseModel):
    title = models.CharField(_("Title"), max_length=200)
    order = models.IntegerField(_("Order"))
    image = models.ImageField(_("Image"), upload_to='videos/')
    duration = models.DurationField(_("Duration"))
    description = models.TextField(_("Description"))

    module = models.ForeignKey("Module", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return f"{self.title}"

