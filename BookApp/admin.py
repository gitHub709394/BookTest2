from django.contrib import admin
from .models import *

# Register your models here.
# 注册模型


# class HeroInfoInLine(admin.TabularInline): # 表格
class HeroInfoInLine(admin.StackedInline):
    model = HeroInfo
    extra = 3

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["bTitle","bPubDate"]
    inlines = [HeroInfoInLine]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
