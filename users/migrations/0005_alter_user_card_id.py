# Generated by Django 4.2.11 on 2024-04-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_card_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card_id',
            field=models.IntegerField(),
        ),
    ]
