from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'email', 'password1', 'password2')