from django.db import models
from django.contrib import admin
# Create your models here.
class Bus(models.Model):
    Busno = models.IntegerField(primary_key=True, help_text="Busno")
    driver=models.CharField(max_length=100)
    From=models.CharField(max_length=100)
    To=models.CharField(max_length=100)
    noofseats=models.IntegerField()
class Businfo(admin.ModelAdmin):
    list_display = ('Busno','driver','From','To','noofseats')    
