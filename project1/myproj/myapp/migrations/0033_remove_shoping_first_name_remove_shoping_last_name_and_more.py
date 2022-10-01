# Generated by Django 4.0.6 on 2022-09-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_remove_shoping_user_alter_kidsproduct_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoping',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='shoping',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='shoping',
            name='password',
        ),
        migrations.AddField(
            model_name='shoping',
            name='city',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AddField(
            model_name='shoping',
            name='state',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AddField(
            model_name='shoping',
            name='zipcode',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='shoping',
            name='address',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='shoping',
            name='name',
            field=models.CharField(default=0, max_length=10),
        ),
    ]