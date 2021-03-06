# Generated by Django 4.0 on 2021-12-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0010_alter_transaction_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='auth_type',
            field=models.CharField(choices=[('SYSTEM', 'system'), ('BIOMETRICS', 'biometrics'), ('RFID', 'rfid')], default='BIOMETRICS', max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_amount',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_title',
            field=models.CharField(default='Error!!!', max_length=255, null=True),
        ),
    ]
