from django.contrib import admin
from .models import Article,Comment
# Register your models here.
class CommentInline(admin.TabularInline) :
    model = Comment
    extra =0
    

class Article_Admin(admin.ModelAdmin) :
    inlines= [
        CommentInline,
    ]
    
    list_display= ["title","author","pk"]


admin.site.register(Article,Article_Admin)
admin.site.register(Comment,)