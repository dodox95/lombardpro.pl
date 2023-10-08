from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Client
from django.shortcuts import render, redirect
from .forms import ClientForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Loan
from .forms import ClientForm, LoanForm
from django.contrib import messages
from django.contrib.auth.models import User
from allauth.account.views import PasswordChangeView
from allauth.account.models import EmailAddress
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# views.py
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

# views.py
from allauth.account.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

login_view = CustomLoginView.as_view()


@login_required
def email_addresses(request):
    if request.method == 'POST':
        # Możesz dodać logikę do dodawania nowego adresu e-mail
        # i wysyłania wiadomości weryfikacyjnej
        pass

    email_addresses = EmailAddress.objects.filter(user=request.user)
    return render(request, 'email_addresses.html', {'email_addresses': email_addresses})


@login_required
def custom_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important, to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('custom_password_change')  # Redirect back to the same page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {'form': form})


@login_required
def main(request):
    return render(request, 'main.html')


@login_required
def my_clients(request):
    clients = request.user.clients.all()
    return render(request, 'my_clients.html', {'clients': clients})

@login_required
def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('my_clients')
    return redirect('my_clients')  # tu można dodać komunikat o błędzie

@login_required
def delete_client(request, client_id=None):
    if request.method == "POST" or client_id is not None:
        if client_id is None:
            client_id = request.POST.get("client_id")
        client = Client.objects.filter(id=client_id, user=request.user).first()
        if client:
            client.delete()
            return redirect('my_clients')
    return redirect('my_clients')  # Redirect with an error message if needed.

def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('my_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'your_template_name.html', {'form': form, 'client': client})

@login_required
def my_loans(request):
    loans = request.user.loans.all()
    query = request.GET.get("q")
    filter_type = request.GET.get("filter", "contract_number")

    if query:
        if filter_type == "contract_number":
            loans = loans.filter(contract_number__icontains=query)
        elif filter_type == "client":
            loans = loans.filter(client__name__icontains=query)  # Zakładając, że model Client ma pole 'name'
        elif filter_type == "precision":
            loans = loans.filter(precision__icontains=query)
        elif filter_type == "loan_amount":
            loans = loans.filter(loan_amount__icontains=query)
        elif filter_type == "interest_rate":
            loans = loans.filter(interest_rate__icontains=query)
        elif filter_type == "current_pickup_amount":
            loans = loans.filter(current_pickup_amount__icontains=query)
        elif filter_type == "contract_date":
            loans = loans.filter(contract_date__icontains=query)
        elif filter_type == "current_due_date":
            loans = loans.filter(current_due_date__icontains=query)
        # Możesz dodać więcej filtrów tutaj

    clients = request.user.clients.all()
    return render(request, 'my_loans.html', {'loans': loans, 'clients': clients})

@login_required
def add_loan(request):
    form = LoanForm()
    show_success_modal = False
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.save()
            show_success_modal = True
            return render(request, 'my_loans.html', {'form': form, 'show_success_modal': show_success_modal})
        else:
            messages.error(request, 'Nie udało się dodać pożyczki.')
    return render(request, 'my_loans.html', {'form': form})

@login_required
def delete_loan(request, loan_id):
    loan = Loan.objects.filter(id=loan_id, user=request.user).first()
    if loan:
        loan.delete()
        return redirect('my_loans')
    return redirect('my_loans')  # Redirect with an error message if needed.

@login_required
def edit_loan(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, user=request.user)
    if request.method == "POST":
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('my_loans')
    else:
        form = LoanForm(instance=loan)
    return render(request, 'loan_edit_template.html', {'form': form, 'loan': loan})

@login_required
def edit_loan(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, user=request.user)
    if request.method == "POST":
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('my_loans')
    else:
        form = LoanForm(instance=loan)
    return render(request, 'my_loans.html', {'form': form, 'loan': loan})

@login_required
def user_profile(request):
    if request.method == "POST":
        # Tu możesz dodać logikę do edycji danych użytkownika
        pass
    return render(request, 'user_profile.html', {'user': request.user})

from django.contrib import messages

@login_required
def user_profile(request):
    if request.method == "POST":
        # Pobierz nową nazwę użytkownika z formularza
        new_username = request.POST.get('username')
        
        # Sprawdź, czy taka nazwa użytkownika już istnieje
        if User.objects.filter(username=new_username).exclude(pk=request.user.pk).exists():
            messages.error(request, 'Nazwa użytkownika jest już zajęta.')
        else:
            request.user.username = new_username
            request.user.save()
            messages.success(request, 'Nazwa użytkownika została zaktualizowana.')
    
    return render(request, 'user_profile.html', {'user': request.user})

from django.shortcuts import render

def email_view(request):
    # Możesz dodać dodatkową logikę tutaj, jeśli jest potrzebna
    return render(request, 'email.html')

def change_loan_status(request, loan_id):
    if request.method == 'POST':
        loan = get_object_or_404(Loan, id=loan_id)
        new_status = request.POST.get('loan_status')
        if new_status in [choice[0] for choice in Loan.STATUS_CHOICES]:
            loan.status = new_status
            loan.save()
    return redirect('the_view_name_to_redirect_to')

