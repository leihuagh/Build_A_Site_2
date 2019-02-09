from django.contrib import admin
from .models import Question, Choice


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    search_fields = ['__str__', 'status']
    list_display = ['__str__', 'status', 'created_by', 'created', 'updated']
    list_filter = ['created_by', 'status']
    readonly_fields = ['created', 'updated']

    class Meta:
        model = Question


admin.site.register(Question, ProfileAdmin)


admin.site.register(Choice)
