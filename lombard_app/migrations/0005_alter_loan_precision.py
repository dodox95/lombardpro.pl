# Generated by Django 4.2.5 on 2023-09-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lombard_app', '0004_remove_client_loan_amount_remove_client_pawn_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='precision',
            field=models.CharField(max_length=255),
        ),
    ]