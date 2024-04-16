# Generated by Django 4.2.11 on 2024-04-15 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_transactions_transfers_remove_log_user_delete_card_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfers',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account'),
        ),
        migrations.AddField(
            model_name='transfers',
            name='transaction',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.transactions', to_field='transaction_id'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account', to_field='card_id'),
        ),
    ]
