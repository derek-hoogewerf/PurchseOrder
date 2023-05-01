from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Requests, Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(Requests)