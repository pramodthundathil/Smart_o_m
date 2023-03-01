# Generated by Django 3.2.8 on 2021-10-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('emp_title', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=20)),
                ('user_name', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
