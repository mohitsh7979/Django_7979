# Generated by Django 4.0.6 on 2022-09-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_kidsproduct_image_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kidsproduct',
            name='image',
            field=models.ImageField(upload_to='kidsimg/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='menimg/images'),
        ),
        migrations.AlterField(
            model_name='womenproduct',
            name='image',
            field=models.ImageField(upload_to='womenimg/images'),
        ),
    ]
