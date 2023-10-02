# Generated by Django 4.2.5 on 2023-09-30 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lombard_app', '0003_rename_price_client_loan_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='loan_amount',
        ),
        migrations.RemoveField(
            model_name='client',
            name='pawn_date',
        ),
        migrations.RemoveField(
            model_name='client',
            name='pickup_date',
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=100, unique=True)),
                ('precision', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contract_date', models.DateField()),
                ('due_date', models.DateField()),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pickup_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=False)),
                ('comments', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='lombard_app.client')),
            ],
        ),
    ]
