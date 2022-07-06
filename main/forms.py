from django import forms
from django.contrib.auth.models import User
from .models import Anketa, DrumKit


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class TrackForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = ('name', 'bpm', 'image', 'audio', 'genre', 'tonal', 'price')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'bpm': forms.TextInput(attrs={'class': 'form-input'}),
            'audio': forms.FileInput(attrs={'accept': '.mp3,.wav'}),
        }


class DrumKitForm(forms.ModelForm):
    class Meta:
        model = DrumKit
        fields = ['name', 'file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.rar,.zip,.7z'})
        }

