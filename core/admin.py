from django.contrib import admin
from .models import Author, Categories, Journal

admin.site.register(Author)
admin.site.register(Categories)
admin.site.register(Journal)
