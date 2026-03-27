from django.contrib import admin
from home.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duedate', 'timestamp', 'author','updated_at')


admin.site.register(Task , TaskAdmin)