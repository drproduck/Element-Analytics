from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']