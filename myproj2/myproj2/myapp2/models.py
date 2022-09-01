from distutils.command.upload import upload
from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='pictures')

    class Meta:
        db_table="profile"

# Create your models here.