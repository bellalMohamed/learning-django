from django.contrib import admin
from blat.models import Blat
# Register your models here.
class BlatAdmin(admin.ModelAdmin):
	list_display = ['text', 'via', 'created_on']
	list_filter = ['created_on']
	search_fields = ['text']

admin.site.register(Blat, BlatAdmin)