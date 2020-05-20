from django import forms
from django.core.validators import MinLengthValidator, FileExtensionValidator
from django_select2 import forms as s2forms

from accounts.models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    sex = forms.ChoiceField(
        label='Пол',
        choices=CustomUser.SEX_CHOICES,
        widget=forms.RadioSelect,
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'sex', 'username', 'password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserPhotoLoadForm(forms.Form):

    photo = forms.FileField(
        label='Photo',
        validators=[FileExtensionValidator(allowed_extensions=CustomUser.VALID_IMAGE_EXTENSIONS)]
    )
