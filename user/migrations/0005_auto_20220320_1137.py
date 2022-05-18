# Generated by Django 3.2.5 on 2022-03-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_rfid_auth_attempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='daily_transaction_limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='limit_charges',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='pos_enabled',
            field=models.BooleanField(default=True),
        ),
    ]