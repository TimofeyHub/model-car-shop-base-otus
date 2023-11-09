from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from myauth.forms import MyUserCreationForm
from myauth.models import MyUser


class MyUserCreateView(CreateView):
    model = MyUser
    success_url = '/'
    form_class = MyUserCreationForm
