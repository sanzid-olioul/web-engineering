from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User,UserProfile

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','date_of_birth','user_type','is_verified']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','date_of_birth','user_type','is_verified']

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "More Info"
    max_num=1
    min_num=1
    add_fieldsets = [
        (
            'More User Info',
            {
                "fields": ['avater','cover_photo','user_wallet','country','subscription_ends'],
            },
        ),
    ]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email','first_name','last_name','date_of_birth','user_type','is_verified']
    list_filter = ['user_type','is_verified','date_of_birth']
    list_editable = ['is_verified']
    fieldsets = [
        (None, {"fields": ['first_name','last_name','email','password',]}),
        ("Personal info", {"fields": ['date_of_birth']}),
        ("Recognition", {"fields": ['user_type','is_verified']}),
    ]

    add_fieldsets = [
        (
            'Basic User Info',
            {
                "fields": ['first_name','last_name','email','password1','password2','date_of_birth','user_type','is_verified'],
            },
        ),
    ]
    search_fields = ['email','first_name','last_name']
    ordering = ['first_name','last_name','email']
    filter_horizontal = []
    inlines = [UserProfileInline]

