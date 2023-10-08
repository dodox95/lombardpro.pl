from django import forms
from .models import Client, Loan

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'id_card', 'country', 'city', 'street', 'status', 'notes']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['contract_number', 'client', 'precision', 'contract_date', 'due_date', 'loan_amount', 'interest_rate', 'pickup_amount', 'status', 'comments']
        widgets = {
            'status': forms.Select(choices=Loan.STATUS_CHOICES)
        }
