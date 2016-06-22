from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from trainer.models import Language


class AddWordForm(forms.Form):
    language = forms.ModelChoiceField(queryset=Language.objects.all())
    word = forms.CharField(required=True)

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

        def save(self, commit=True):
            user = super(UserCreateForm,self).save(commit=False)
            user.email = self.cleaned_data["email"]
            user.name = self.cleaned_data["first_name"]
            user.prename = self.cleaned_data["last_name"]

            if commit:
                user.save()

            return user

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())


class UploadFileForm(forms.Form):
    language = forms.ModelChoiceField(label='Language', queryset=Language.objects.all(), required=True)
    file = forms.FileField(required=True)