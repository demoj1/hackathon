from registration.forms import RegistrationForm
from app.models import UserProfile
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)


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
        fields = ('username', 'group', 'first_name', 'last_name',)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-5'

    helper.layout = Layout(
        Field('username', css_class='input-sm'),
        Field('first_name', css_class='input-sm'),
        Field('last_name', css_class='input-sm'),
        Field('email', css_class='input-sm'),
        Field('group', css_class='input-sm'),
        Field('password1', css_class='input-sm'),
        Field('password2', css_class='input-sm'),
        FormActions(Submit("Регистрация", "Регистрация", css_class='btn-primary'))
    )
