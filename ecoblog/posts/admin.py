from django.contrib import admin

# Register your models here.
from .models import Post, Stocks, Input

admin.site.register(Post)
admin.site.register(Stocks)
admin.site.register(Input)
