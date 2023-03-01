from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_nam","last_name","username","password1","password2"]