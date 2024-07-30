from django.contrib import admin

from .models import News, About


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
