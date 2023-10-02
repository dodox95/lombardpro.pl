from django.contrib import admin
from django.urls import path, include
from lombard_app import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.main, name='main'),  # This makes the main view the default for the root URL
    path('my_clients/', views.my_clients, name='my_clients'),
    path('my_loans/', views.my_loans, name='my_loans'),
    
    path('add_client/', views.add_client, name='add_client'),
    path('add_loan/', views.add_loan, name='add_loan'),
    path('delete_client/', views.delete_client, name='delete_client_without_id'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client_with_id'),
    path('edit_client/<int:client_id>/', views.edit_client, name='edit_client'),
]
