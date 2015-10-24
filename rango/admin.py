from django.contrib import admin
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User


class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url')

class CatAdmin(admin.ModelAdmin):
	list_display = ('name','views','likes','slugs')
	prepopulated_fields = {'slugs':('name',)}

admin.site.register(Category,CatAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
#admin.site.register(User)