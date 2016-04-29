from registration.forms import RegistrationForm
from app.models import UserProfile
from django import forms


class CustomUserForm(RegistrationForm):
    username = forms.CharField(max_length=30, required=True, label="Имя пользователя")
    first_name = forms.CharField(max_length=30, required=True, label="Имя")
    last_name = forms.CharField(max_length=30, required=True, label="Фамилия")
    email = forms.EmailField(required=True, label="E-mail")
    group = forms.CharField(required=True, label="Группа")
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = UserProfile
        fields = ('username', 'group', 'first_name', 'last_name', 'email',)

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "email", "group",)

