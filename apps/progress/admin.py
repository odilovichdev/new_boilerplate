from django.contrib import admin

from .models import (
    UserCourseBought,
    UserCourseRating,
    UserVideoDuration
)


@admin.register(UserCourseBought)
class UserCourseBoughtAdmin(admin.ModelAdmin):
    pass


@admin.register(UserCourseRating)
class UserCourseRatingAdmin(admin.ModelAdmin):
    pass


@admin.register(UserVideoDuration)
class UserVideoDurationAdmin(admin.ModelAdmin):
    pass
