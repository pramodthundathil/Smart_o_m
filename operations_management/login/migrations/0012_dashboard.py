# Generated by Django 3.2.8 on 2021-10-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_alter_leave_approve_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='dashboard',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=1000)),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
