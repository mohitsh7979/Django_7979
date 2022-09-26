# Generated by Django 4.0.6 on 2022-09-24 08:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0021_rename_cart_kcart_wcart_mcart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mcart',
            new_name='cart',
        ),
        migrations.RemoveField(
            model_name='wcart',
            name='kproduct',
        ),
        migrations.RemoveField(
            model_name='wcart',
            name='mproduct',
        ),
        migrations.RemoveField(
            model_name='wcart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wcart',
            name='wproduct',
        ),
        migrations.DeleteModel(
            name='kcart',
        ),
        migrations.DeleteModel(
            name='wcart',
        ),
    ]
