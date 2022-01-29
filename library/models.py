from django.db import models
from django.forms import ModelForm,Textarea

# Create your models here.

class Books(models.Model):
    auto_id= models.AutoField(auto_created=True , primary_key=True, serialize=False, verbose_name='ID')
    isbn=models.CharField(max_length=100)
    title=models.CharField(max_length=250)
    authors=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    price=models.FloatField()
    

    