# Generated by Django 3.2.23 on 2024-01-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('ink slinger', 'Ink Slinger'), ('ink addict', 'Ink Addict'), ('looking for inspo', 'Looking for Inspo')], max_length=50),
        ),
    ]
