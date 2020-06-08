from django.contrib import admin
from useraccount.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        *BaseUserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Additional Details',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': ('is_admin','image','organization'),
            },
        ),
    )


admin.site.register(User,UserAdmin)



