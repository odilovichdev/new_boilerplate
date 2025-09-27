from django.contrib import admin

from .models import (
    Book,
    BookLanguage,
    BookCategory
)

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BookLanguage)
class BookLanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

