from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserChangeForm(admin_forms.UserChangeForm):
    class Meta:
        model=User
        fields='__all__'

class UserCreationForm(admin_forms.UserCreationForm):
    class Meta:
        model=User
        fields=("first_name","last_name","email")
    
    error_messages={
        "duplicate_email" : _("A User with this email already exists.")
    }

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages["duplicate_email"])