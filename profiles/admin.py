from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile
from .models import *

# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    # fieldsets = [
    #     ('Personal info', {'fields': ['postal_code', ]}),
    # ]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
