from django.contrib import admin
from .models import News, Categories, Comment

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(News, NewsAdmin)
admin.site.register(Categories)
admin.site.register(Comment)
