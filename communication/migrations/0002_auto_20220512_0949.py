# Generated by Django 3.2.5 on 2022-05-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='read_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='received_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]