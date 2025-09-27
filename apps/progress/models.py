from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

Users = get_user_model()


class UserVideoDuration(BaseModel):
    duration = models.DurationField(_("Durations"))
    finished = models.BooleanField(_("Finished"), default=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey("courses.Video", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("User Video Duration")
        verbose_name_plural = _("User Video Durations")

    def __str__(self):
        return f"{self.user_id | self.video_id}"


class UserCourseRating(BaseModel):
    rating = models.IntegerField(_("Rating"))
    description = models.TextField(_("Description"))
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="user_courses_rating")
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="user_courses_rating")

    class Meta:
        verbose_name = _("User Course Rating")
        verbose_name_plural = _("Users Course Ratings")

    def __str__(self):
        return f"{self.user_id | self.course_id}"


class UserCourseBought(BaseModel):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="user_courses_bought")
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="user_courses_bought")

    class Meta:
        verbose_name = _("User Course Bought")
        verbose_name_plural = _("Users Course Boughts")

    def __str__(self):
        return f"{self.user_id | self.course_id}"
