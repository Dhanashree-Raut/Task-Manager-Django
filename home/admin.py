from django.contrib import admin
from home.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duedate', 'timestamp', 'created_at','updated_at')


admin.site.register(Task , TaskAdmin)