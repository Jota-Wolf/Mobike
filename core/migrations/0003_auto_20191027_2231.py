# Generated by Django 2.2.6 on 2019-10-28 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191027_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='numero',
            new_name='telefono',
        ),
    ]
