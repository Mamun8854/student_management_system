# Generated by Django 4.2.4 on 2023-08-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=100, null=True)),
                ('stident_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('student_roll', models.IntegerField(blank=True, max_length=20, null=True)),
                ('student_phone', models.IntegerField(blank=True, max_length=20, null=True)),
                ('department', models.CharField(blank=True, max_length=30, null=True)),
                ('semester', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
