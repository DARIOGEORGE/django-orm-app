# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve bus information using ORM .

## Entity Relationship Diagram

### Bus Information Entity Diagram

![entity](https://user-images.githubusercontent.com/118704873/209542725-056b9182-2b99-4c51-a1d8-87d9d7c48cbd.png)




## DESIGN STEPS

### STEP 1:
Clone the repository to theia ide. start a new app inside the project folder.

### STEP 2:
Type the appropriate code for your table and provide appropriate data types to the columns.
### STEP 3:
Create a report about your project in readme.md file and upload the django.orm.app folder to your remote repository.

## PROGRAM
```
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

```
## OUTPUT

### Businfo Table
![output-orm](https://user-images.githubusercontent.com/118704873/209543889-9c49ef16-157b-4c50-ae0c-74da97039e0a.png)




## RESULT
Thus the project is developed to have Bus information database
