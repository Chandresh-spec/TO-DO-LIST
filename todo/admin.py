from django.contrib import admin
from.models import Task
# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display=('text','created_date')
    search_fields=('text',)
    ordering=('created_date',)


admin.site.register(Task,ToDoAdmin)