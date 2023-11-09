from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myauth.models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'full_name', 'phone_number', 'password1', 'password2')
