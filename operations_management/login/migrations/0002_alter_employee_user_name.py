# Generated by Django 3.2.8 on 2021-10-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
