# Generated by Django 4.0 on 2021-12-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_alter_pos_options_alter_pos_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
