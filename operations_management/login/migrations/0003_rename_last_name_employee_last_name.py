# Generated by Django 3.2.8 on 2021-10-13 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_employee_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Last_name',
            new_name='last_name',
        ),
    ]
