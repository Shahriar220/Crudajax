from django.contrib import admin

from .models import CrudUser

class CrudUserAdmin(admin.ModelAdmin):
	list_display=('id','name','address','phone')
	list_display_links=('id',)
	list_filter=('name',)
	list_editable=('name','address','phone')
	search_fileds=('name','address','phone')
	list_per_page=25

admin.site.register(CrudUser,CrudUserAdmin)


