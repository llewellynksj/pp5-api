# Generated by Django 3.2.23 on 2024-01-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_tags',
            field=models.CharField(blank=True, choices=[('tribal', 'Tribal'), ('geometric', 'Geometric'), ('realism', 'Realism'), ('portraits', 'Portraits'), ('illustrative', 'Illustrative'), ('dotwork', 'Dotwork'), ('watercolour', 'Watercolour'), ('neo-traditional', 'Neo-traditional'), ('abstract', 'Abstract'), ('animals', 'Animals'), ('lettering', 'Lettering'), ('traditional', 'Traditional')], max_length=50, null=True),
        ),
    ]
