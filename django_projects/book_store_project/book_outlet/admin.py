from django.contrib import admin
from .models import Book, Author, Address, Country


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "rating")
    search_fields = ("title", "author")
    list_filter = ("author", "rating")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
