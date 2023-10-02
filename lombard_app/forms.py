from django import forms
from .models import Client, Loan

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'id_card', 'country', 'city', 'street', 'status', 'notes']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'  # includes all fields from the Loan model
