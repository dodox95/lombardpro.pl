from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Client, Loan
from django.shortcuts import render, redirect
from .forms import ClientForm, LoanForm  # zakład
import os
from django.shortcuts import render, redirect, get_object_or_404
import datetime


@login_required
def main(request):
    return render(request, 'main.html')

@login_required
def my_clients(request):
    clients = request.user.clients.all()
    return render(request, 'my_clients.html', {'clients': clients})

@login_required
def my_loans(request):
    loans = request.user.loans.all()
    clients = request.user.clients.all()  # Added this line
    return render(request, 'my_loans.html', {'loans': loans, 'clients': clients})


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



def add_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            # maybe add a success message or notification
            return redirect('my_loans')
    else:
        form = LoanForm()

    # If the form isn't valid or it's a GET request, show the form
    return render(request, 'add_loan_form.html', {'form': form})



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


# views.py
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
