# Generated by Django 4.2.5 on 2023-09-30 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lombard_app', '0002_remove_client_weight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='price',
            new_name='loan_amount',
        ),
    ]
