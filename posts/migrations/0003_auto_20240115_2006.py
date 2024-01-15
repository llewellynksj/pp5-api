# Generated by Django 3.2.23 on 2024-01-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='caption',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_tags',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='image_tag',
            field=models.CharField(blank=True, choices=[('tribal', 'Tribal'), ('geometric', 'Geometric'), ('realism', 'Realism'), ('portraits', 'Portraits'), ('illustrative', 'Illustrative'), ('dotwork', 'Dotwork'), ('watercolour', 'Watercolour'), ('neo-traditional', 'Neo-traditional'), ('abstract', 'Abstract'), ('animals', 'Animals'), ('lettering', 'Lettering'), ('traditional', 'Traditional')], max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='image_tag2',
            field=models.CharField(blank=True, choices=[('tribal', 'Tribal'), ('geometric', 'Geometric'), ('realism', 'Realism'), ('portraits', 'Portraits'), ('illustrative', 'Illustrative'), ('dotwork', 'Dotwork'), ('watercolour', 'Watercolour'), ('neo-traditional', 'Neo-traditional'), ('abstract', 'Abstract'), ('animals', 'Animals'), ('lettering', 'Lettering'), ('traditional', 'Traditional')], max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='image_tag3',
            field=models.CharField(blank=True, choices=[('tribal', 'Tribal'), ('geometric', 'Geometric'), ('realism', 'Realism'), ('portraits', 'Portraits'), ('illustrative', 'Illustrative'), ('dotwork', 'Dotwork'), ('watercolour', 'Watercolour'), ('neo-traditional', 'Neo-traditional'), ('abstract', 'Abstract'), ('animals', 'Animals'), ('lettering', 'Lettering'), ('traditional', 'Traditional')], max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='image_tag4',
            field=models.CharField(blank=True, choices=[('tribal', 'Tribal'), ('geometric', 'Geometric'), ('realism', 'Realism'), ('portraits', 'Portraits'), ('illustrative', 'Illustrative'), ('dotwork', 'Dotwork'), ('watercolour', 'Watercolour'), ('neo-traditional', 'Neo-traditional'), ('abstract', 'Abstract'), ('animals', 'Animals'), ('lettering', 'Lettering'), ('traditional', 'Traditional')], max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='image_tag5',
            field=models.CharField(blank=True, choices=[('tribal', 'Tribal'), ('geometric', 'Geometric'), ('realism', 'Realism'), ('portraits', 'Portraits'), ('illustrative', 'Illustrative'), ('dotwork', 'Dotwork'), ('watercolour', 'Watercolour'), ('neo-traditional', 'Neo-traditional'), ('abstract', 'Abstract'), ('animals', 'Animals'), ('lettering', 'Lettering'), ('traditional', 'Traditional')], max_length=50),
        ),
    ]