from django.contrib import admin
from .models import Author, review, iPhoneCategory, iPhoneModel

# Registered models here

admin.site.register(Author)
admin.site.register(review)
admin.site.register(iPhoneCategory)
admin.site.register(iPhoneModel)
