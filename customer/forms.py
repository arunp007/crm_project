from django import forms
from accounts.models import Customer, Technician
from customer.models import Complaint, SalesOrder

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'address', 'phone', 'email', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'class' : 'form-control',}),
            'address': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'password':  forms.TextInput(attrs={'class' : 'form-control'}),
        }


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['complaint_id', 'complaint_date', 'customer_type', 'complaint_type', 'technician', 'token', 'token_number', 'machine_type', 'machine_model', 'machine_no', 'payment_status', 'payment_type', 'collected_amount', 'ticket_status', 'is_resolve']
        widgets = {
            'complaint_id': forms.TextInput(attrs={'class': 'form-control' }),
            'complaint_date': forms.DateInput(attrs = {'class': 'form-control', 'type': 'date',}),
        }

    def __init__(self, *args, **kwargs):
        #hide and show fields
        show_fields = kwargs.pop('show_fields', {})
        super().__init__(*args, **kwargs)

        #hide and show fields

        if show_fields.get('technician'):
            self.fields['technician'].required = True
            self.fields['technician'].queryset = Technician.objects.all()
            self.fields['technician'].widget.attrs.update({'class': 'form-control'})
        
        else:
            self.fields['technician'].required = False
            self.fields['technician'].widget = forms.HiddenInput()  # Hide the field

        if show_fields.get('token'):
            self.fields['token'].required = True
            self.fields['token'].widget = forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})

        else:
            self.fields['token'].required = False
            self.fields['token'].widget = forms.HiddenInput() 

        if show_fields.get('token_number'):
            self.fields['token_number'].required = True
            self.fields['token_number'].widget = forms.NumberInput(attrs={'class': 'form-control'})

        else:
            self.fields['token_number'].required = False
            self.fields['token_number'].widget = forms.HiddenInput()

        if show_fields.get('machine_type'):
            self.fields['machine_type'].required = True
            self.fields['machine_type'].widget = forms.TextInput(attrs={'class': 'form-control'})

        else:
            self.fields['machine_type'].required = False
            self.fields['machine_type'].widget = forms.HiddenInput()

        if show_fields.get('machine_model'):
            self.fields['machine_model'].required = True
            self.fields['machine_model'].widget = forms.TextInput(attrs={'class': 'form-control'})

        else:
            self.fields['machine_model'].required = False
            self.fields['machine_model'].widget = forms.HiddenInput()

        if show_fields.get('machine_no'):
            self.fields['machine_no'].required = True
            self.fields['machine_no'].widget = forms.TextInput(attrs={'class': 'form-control'})

        else:
            self.fields['machine_no'].required = False
            self.fields['machine_no'].widget = forms.HiddenInput()

        if show_fields.get('payment_status'):
            self.fields['payment_status'].required = True
            self.fields['payment_status'].widget = forms.Select(choices=Complaint.PAYMENT_STATUS ,attrs={'class': 'form-control'})

        else:
            self.fields['payment_status'].required = False
            self.fields['payment_status'].widget = forms.HiddenInput()
        
        if show_fields.get('payment_type'):
            self.fields['payment_type'].required = True
            self.fields['payment_type'].widget = forms.Select(choices=Complaint.PAYMENT_TYPE ,attrs={'class': 'form-control'})

        else:
            self.fields['payment_type'].required = False
            self.fields['payment_type'].widget = forms.HiddenInput()
        
        if show_fields.get('collected_amount'):
            self.fields['collected_amount'].required = True
            self.fields['collected_amount'].widget = forms.TextInput(attrs={'class': 'form-control'})

        else:
            self.fields['collected_amount'].required = False
            self.fields['collected_amount'].widget = forms.HiddenInput()

        if show_fields.get('ticket_status'):
            self.fields['ticket_status'].required = True
            self.fields['ticket_status'].widget = forms.Select(choices=Complaint.TICKET_STATUS ,attrs={'class': 'form-control'})

        else:
            self.fields['ticket_status'].required = False
            self.fields['ticket_status'].widget = forms.HiddenInput()

        if show_fields.get('is_resolve'):
            self.fields['is_resolve'].initial = False
            self.fields['is_resolve'].widget = forms.CheckboxInput()

        else:
            self.fields['is_resolve'].required = False
            self.fields['is_resolve'].widget = forms.HiddenInput()


       



        self.fields['customer_type'].widget = forms.Select(choices=Complaint.CUSTOMER_TYPE_CHOICES, attrs={'class': 'form-control'})
        self.fields['complaint_type'].widget = forms.Select(choices=Complaint.COMPLAINT_TYPE_CHOICES, attrs={'class': 'form-control'})
        
        

class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['current_date', 'follow_up_date', 'name', 'designation', 'mobile', 'email', 'reference', 'status']
        widgets = {
            'current_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'follow_up_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'reference': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reference'].widget = forms.Select(choices=SalesOrder.REFERENCE_CHOICES, attrs={'class': 'form-control'})
        self.fields['status'].widget = forms.Select(choices=SalesOrder.STATUS_CHOICES, attrs={'class': 'form-control'})