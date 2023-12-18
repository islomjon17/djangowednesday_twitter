from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep

# Unregestered groups
admin.site.unregister(Group)

# Mix profile info to user info


class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User  model
class UserAdmin(admin.ModelAdmin):
    model = User    
    # Jsuer display username fields
    fields = ["username"]
    inlines = [ProfileInline]
# Unregestered user
admin.site.unregister(User)

# Regestered user
admin.site.register(User, UserAdmin)

# Regestered Meeps
admin.site.register(Meep)















# Register your models here.
