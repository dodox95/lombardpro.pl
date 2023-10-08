from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_card = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    notes = models.TextField(blank=True, default='')
    
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='clients')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Loan(models.Model):
    contract_number = models.CharField(max_length=100, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='loans')
    precision = models.CharField(max_length=255)  # Określ odpowiednią długość max dla tego pola
    contract_date = models.DateField()
    due_date = models.DateField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # np. 5.25 dla 5.25%
    pickup_amount = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='loans')
    STATUS_CHOICES = (
        ('active', 'Aktywna'),
        ('extended', 'Przedłużona'),
        ('picked_up', 'Odebrana'),
        ('deadline_passed', 'Termin minął'),
        ('inactive', 'Nieaktywna'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')


    def current_due_date(self):
        latest_extension = self.extensions.order_by('-new_due_date').first()
        return latest_extension.new_due_date if latest_extension else self.due_date
    
    def current_pickup_amount(self):
        total_extension_fee = sum(ext.extension_fee for ext in self.extensions.all())
        return self.pickup_amount + total_extension_fee
    
    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"

class Extension(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='extensions')
    extension_date = models.DateField(auto_now_add=True)
    new_due_date = models.DateField()
    extension_fee = models.DecimalField(max_digits=5, decimal_places=2)
