# Generated by Django 4.0 on 2021-12-26 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pos',
            old_name='isActive',
            new_name='is_active',
        ),
    ]
