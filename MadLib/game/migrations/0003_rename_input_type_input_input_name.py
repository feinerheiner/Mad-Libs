# Generated by Django 4.2.3 on 2023-07-30 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_input_input_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='input_type',
            new_name='input_name',
        ),
    ]
