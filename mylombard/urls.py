from django.contrib import admin
from django.urls import path, include
from lombard_app import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('accounts/login/', views.login_view, name='account_login'),
    path('custom_password_change/', views.custom_password_change, name='custom_password_change'),

    path('', views.main, name='main'),  # This makes the main view the default for the root URL
    path('my_clients/', views.my_clients, name='my_clients'),
    
    path('add_client/', views.add_client, name='add_client'),
    path('delete_client/', views.delete_client, name='delete_client_without_id'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client_with_id'),
    path('edit_client/<int:client_id>/', views.edit_client, name='edit_client'),
    
    path('my_loans/', views.my_loans, name='my_loans'),
    path('add_loan/', views.add_loan, name='add_loan'),
    path('delete_loan/<int:loan_id>/', views.delete_loan, name='delete_loan'),
    path('edit_loan/<int:loan_id>/', views.edit_loan, name='edit_loan'),
    path('edit_loan/<int:loan_id>/', views.edit_loan, name='edit_loan'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('accounts/email/', views.email_view, name='email'),
    path('change_loan_status/<int:loan_id>/', views.change_loan_status, name='your_view_name_to_change_status'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)