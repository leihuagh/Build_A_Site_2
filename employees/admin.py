from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    # date_hierarchy = '-created'
    search_fields = ['__str__', 'designation']
    list_display = ['__str__', 'user_username', 'user_email', 'designation', 'salary',
                    'created', 'updated']
    list_editable = ['salary']
    list_filter = ['designation', 'salary']
    readonly_fields = ['created', 'updated']

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)
