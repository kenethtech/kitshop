# Generated by Django 4.1.2 on 2023-03-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_image_caption_product_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, max_length=200, upload_to='images/products/main'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=200, upload_to='images/products/thumbnails'),
        ),
    ]