from django import forms
from .models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'age']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
        }