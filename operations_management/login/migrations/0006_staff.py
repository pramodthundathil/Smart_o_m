# Generated by Django 3.2.8 on 2021-10-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_employee_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staff_name', models.CharField(max_length=100)),
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_title', models.CharField(max_length=100)),
                ('department_id', models.CharField(max_length=50)),
                ('DOB', models.DateField(auto_now_add=True)),
                ('date_of_join', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
