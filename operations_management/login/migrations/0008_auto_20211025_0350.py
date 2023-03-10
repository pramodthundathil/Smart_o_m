# Generated by Django 3.2.8 on 2021-10-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_staff_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50)),
                ('emp_id', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('leave_start', models.DateField()),
                ('leave_end', models.DateField()),
                ('total_leave', models.CharField(max_length=50)),
                ('approve_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='DOB',
            field=models.DateField(),
        ),
    ]
