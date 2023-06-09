from django.contrib import admin
from . import models


class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 0
    readonly_fields = ['uuid']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'author', 'display_genre']
    inlines = [BookInstanceInline]
    search_fields = ['title', 'author__first_name', 'author__last_name']


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'uuid', 'status', 'due_back', 'reader']
    list_filter = ['status', 'due_back', 'book']
    list_editable = ['status', 'due_back', 'reader']
    search_fields = ['uuid', 'book__title']

    # fieldsets = (
    #     ('General', {'fields': ('uuid', 'book')}),
    #     ('Availability', {'fields': ('status', 'due_back')}),
    # )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'display_books']

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'date_created', 'reviewer', 'content')

# Register your models here.
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookInstance, BookInstanceAdmin)
admin.site.register(models.BookReview, BookReviewAdmin)
admin.site.register(models.Profile)