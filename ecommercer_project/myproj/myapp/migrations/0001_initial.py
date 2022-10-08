# Generated by Django 4.0.6 on 2022-10-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('m', 'men'), ('w', 'women'), ('k', 'kids'), ('mk', 'men kit'), ('wt', 'watch')], max_length=10)),
                ('image', models.ImageField(upload_to='productimage')),
            ],
        ),
    ]
