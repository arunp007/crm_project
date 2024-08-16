from django import forms
from accounts.models import Technician
from technician.models import Receipt

class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['full_name', 'address', 'phone', 'email_id', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'class' : 'form-control',}),
            'address': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email_id' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'password':  forms.TextInput(attrs={'class' : 'form-control'}),
        }


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['receipt_date', 'payment_type', 'receipt_amount']
        
    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)

        self.fields['payment_type'].widget = forms.Select(choices=Receipt.PAYMENT_TYPE, attrs={'class': 'form-control'})
        self.fields['receipt_date'].widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        self.fields['receipt_amount'].widget = forms.TextInput(attrs={'class': 'form-control'})


