from django.contrib import admin
from .models import Issue, Category

admin.site.register(Issue)
admin.site.register(Category)