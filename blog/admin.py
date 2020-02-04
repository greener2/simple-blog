from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget

from blog import models
import django.db.models
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    search_fields = ['title', 'subtitle', 'body', 'author']
    filter_horizontal = ("tags", )

    formfield_overrides = {
        django.db.models.TextField: {"widget": AdminPagedownWidget}
    }


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
