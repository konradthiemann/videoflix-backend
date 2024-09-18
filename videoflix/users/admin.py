from django.contrib import admin
from .models import User
# from .forms import CustomUserCreationForm
# from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
# Register your models here.
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
    
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Custom Fields',
#             {
#                 'fields': (
#                     'custom',
#                     'phone',
#                     'address',
#                 )
#             }
#         )
#     )