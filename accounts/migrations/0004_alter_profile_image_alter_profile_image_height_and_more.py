# Generated by Django 4.2.5 on 2023-10-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_image_height_profile_image_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(height_field='image_height', upload_to='profile/', width_field='image_width'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, help_text='Высота изображения', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, help_text='Ширина изображения', null=True),
        ),
    ]
