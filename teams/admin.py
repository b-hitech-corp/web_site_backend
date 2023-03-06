from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Header)
# class HeaderAdmin(admin.ModelAdmin):
# 	list_headere='__all__'

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	list_member='__all__'
