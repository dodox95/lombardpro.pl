from django.contrib import admin
from .models import Client, Loan, Extension
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "id_card", "country", "city", "street", "status", "number_of_loans"]
    search_fields = ["first_name", "last_name", "id_card"]
    list_filter = ["country", "city", "status"]

    def number_of_loans(self, obj):
        count = obj.loans.count()
        url = reverse('admin:lombard_app_loan_changelist')
        return format_html('<a href="{}?client__id={}">{}</a>', url, obj.id, count)

    number_of_loans.short_description = 'Loans'

class ExtensionInline(admin.TabularInline): 
    model = Extension
    extra = 1  
    fields = ["new_due_date", "extension_fee"]
    
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ["contract_number", "client", "precision", "contract_date", "due_date", "loan_amount", "interest_rate", "pickup_amount", "colored_status", "comments", "current_due_date_display", "current_pickup_amount_display"]
    search_fields = ["contract_number", "client__first_name", "client__last_name"]
    list_filter = ["contract_date", "due_date", "status"]
    inlines = [ExtensionInline]

    def colored_status(self, obj):
        if obj.status:
            return format_html('<span style="color: green;">Received</span>')
        else:
            return format_html('<span style="color: red;">Not received</span>')

    colored_status.admin_order_field = 'status'
    colored_status.short_description = 'Status'
    
    def current_due_date_display(self, obj):
        return obj.current_due_date()
    current_due_date_display.short_description = 'Current Due Date'
    
    def current_pickup_amount_display(self, obj):
        return obj.current_pickup_amount()
    current_pickup_amount_display.short_description = 'Current Pickup Amount'

@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    list_display = ["loan", "extension_date", "new_due_date", "extension_fee"]
    search_fields = ["loan__contract_number", "loan__client__first_name", "loan__client__last_name"]
    list_filter = ["extension_date", "new_due_date"]
