# Generated by Django 4.2 on 2025-02-10 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='age',
            new_name='birthday',
        ),
    ]
