# Generated by Django 4.0.6 on 2022-09-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_remove_order_items_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items_json',
            field=models.CharField(default=0, max_length=5000),
            preserve_default=False,
        ),
    ]
