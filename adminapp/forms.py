from django import forms
from accounts.models import Admin

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['full_name', 'address', 'phone', 'email', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'class' : 'form-control',}),
            'address': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'password':  forms.TextInput(attrs={'class' : 'form-control'}),
        }

