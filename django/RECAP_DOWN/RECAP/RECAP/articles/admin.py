from django.contrib import admin
from .models import Article, Comment, Hashtag

# Register your models here.

# 새로운 클래스를 설정하여 django-admin이 model의 설정을 가져올 수 있도록 만들 수 있다.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    list_display_links = ['title',]

admin.site.register(Article, ArticleAdmin)


# 보충수업
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)

class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Hashtag, HashtagAdmin)