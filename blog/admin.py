from django.contrib import admin
from blog import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    search_fields = ['title', 'subtitle', 'body', 'author']
    filter_horizontal = ("tags", )


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
