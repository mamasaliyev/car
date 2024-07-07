from django.core.exceptions import ValidationError
from django.forms import forms, CharField, ModelForm, Form, FileField

from .models import User


class UserLoginForm(Form):
    username = CharField(max_length=28)
    password = CharField(max_length=28)


class UserRegisterForm(ModelForm):
    password1 = CharField(max_length=28)
    password2 = CharField(max_length=28)
    avatar = FileField()

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError('Passwords must match!')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'avatar')


class UserUpdateForm(ModelForm):
    password1 = CharField(max_length=28)
    password2 = CharField(max_length=28)
    avatar = FileField()

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError('Passwords must be match!')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'avatar')
