# Generated by Django 3.2.8 on 2021-10-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_rename_last_name_employee_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(max_length=12),
        ),
    ]
