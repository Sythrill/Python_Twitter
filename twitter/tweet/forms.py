from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, TextInput

from tweet.models import User, Message, Comment, PersonalMessage


class LoginUserForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=64)
    passwd = forms.CharField(label="Password", widget=forms.PasswordInput)


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")
        if commit:
            user.save()
        return user


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        exclude = ['created_by', 'is_read']
        widgets = {
            'content': TextInput(attrs={'placeholder': 'Type your message here'})
        }
        labels = {
            'content': '',
        }


class AddCommentForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class AddPvrMsgForm(forms.ModelForm):
    class Meta:
        model = PersonalMessage
        fields = "__all__"
        exclude = ["from_user", "to_user"]
        widgets = {
            'content': TextInput(attrs={'placeholder': 'Type your message here'})
        }
        labels = {
            'content': '',
        }

class EditUserForm(forms.ModelForm):
    twitter = forms.CharField(required=False)
    facebook = forms.CharField(required=False)
    google = forms.CharField(required=False)
    behance = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "image", "twitter", "facebook", "google", "behance"]
