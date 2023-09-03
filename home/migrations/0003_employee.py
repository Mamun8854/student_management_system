# Generated by Django 4.2.4 on 2023-09-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_student_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(blank=True, max_length=70, null=True)),
                ('employee_email', models.EmailField(blank=True, max_length=70, null=True)),
                ('employee_phone', models.IntegerField(default=0)),
                ('employee_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
