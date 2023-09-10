from django.contrib import admin
from .models import Author, Book, Review


class AuthorAdmin(admin.ModelAdmin):
	list_filter = ('id',)


class ReviewAdmin(admin.ModelAdmin):
	list_display = ('id', 'rating', 'review_date', 'content', 'user')
	list_display_links = ('id', 'rating')
	search_fields = ('id', 'rating', 'review_date')
	list_filter = ('rating', 'review_date')

class BookAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'publish_date', 'description')
	list_display_links = ('title',)
	search_fields = ('id', 'publish_date')
	list_filter = ('publish_date',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
