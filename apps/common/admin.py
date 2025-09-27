from django.contrib import admin

from .models import (
    Contact,
    CompanyProfile,
    CompanySocialMedia
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(CompanySocialMedia)
class CompanySocialMediaAdmin(admin.ModelAdmin):
    pass

