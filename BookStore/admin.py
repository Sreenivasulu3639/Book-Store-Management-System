from django.contrib import admin

from BookStore.models import Category, Book, Author, City

# Register your models here.
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Author)
admin.site.register(Book)