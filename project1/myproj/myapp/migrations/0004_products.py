# Generated by Django 4.0.6 on 2022-09-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_shoping_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=50)),
                ('image', models.ImageField(default=0, upload_to='')),
            ],
        ),
    ]
