from django import forms
from Modules.Users.Models.User import User, Group
from django.core import validators


class UserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    email = forms.CharField(required=True, validators=[validators.validate_email])
    first_name = forms.CharField()
    phone = forms.CharField(required=False)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all())
    isActive = forms.BooleanField(required=False)
    avatar = forms.ImageField(required=False)
    error_messages = {
        'password_mismatch': "The password fields didn't match.",
    }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'phone', 'groups', 'isActive', 'avatar')


    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user



class UpdateUserForm(forms.ModelForm):
    email = forms.CharField(required=True, validators=[validators.validate_email])
    first_name = forms.CharField()
    phone = forms.CharField(required=False)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all())
    isActive = forms.BooleanField(required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'phone', 'groups', 'isActive', 'avatar')
