from django.contrib import admin
from posts.models import Auther
# Register your models here.
class AutherAdmin(admin.ModelAdmin):
    list_dispaly=['name','email']
admin.site.register(Auther,AutherAdmin)