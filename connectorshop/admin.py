from django.contrib import admin
from .models import userDetail ,Article, Category, Tag

admin.site.register(userDetail)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)