from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from api.user.forms import UserChangeForm, UserCreationForm
from api.user.models import UserProfile


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + tuple(
        auth_admin.UserAdmin.fieldsets
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    model = UserProfile
