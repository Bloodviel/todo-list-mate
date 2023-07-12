from django.contrib import admin
from django.contrib.auth.models import Group

from todo.models import Tag, Task


admin.site.unregister(Group)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "content",
        "mark_task",
        "date_time",
        "deadline"
    ]
    list_filter = ["date_time"]
