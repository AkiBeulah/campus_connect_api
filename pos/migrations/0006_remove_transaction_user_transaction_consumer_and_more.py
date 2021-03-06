# Generated by Django 4.0 on 2021-12-28 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_biometrics_auth_user_biometrics_enabled_and_more'),
        ('pos', '0005_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.AddField(
            model_name='transaction',
            name='consumer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='consumer', to='user.user'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vendor', to='user.user'),
        ),
    ]
