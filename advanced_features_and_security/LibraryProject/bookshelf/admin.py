from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Book, CustomUser, Review, CustomUserAdmin

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display= ['book', 'user', 'review_text']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","publication_year","author"]
    search_fields = ["title"]
    list_filter = ["publication_year"]

#registering the new CustomUserModel
admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)