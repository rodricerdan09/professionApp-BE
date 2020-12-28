from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profesional


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = ('username', 'email', 'last_name', 'first_name')


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profesional
        fields = ('profesion', 'matricula', 'telefono', 'servicio', 'website_url', 'facebook_url', 'instagram_url')