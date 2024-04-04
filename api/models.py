from datetime import timezone
import datetime
from django.db import models

# Create your models here.
# try to understand in a deep way what's a model and what's its utility 
class Tab_aux(models.Model):
    id = models.AutoField(primary_key = True)
    code = models.CharField(max_length = 20)
    libelle = models.CharField(max_length = 255)
    date = models.DateTimeField(default=datetime.datetime.now)

    class Meta: 
     db_table = "Tab_aux"

    def save(self, *args, **kwargs):
        # Update the date field to the current date and time
        self.date = datetime.datetime.now()
        super().save(*args, **kwargs) 



class Tab_com(models.Model): 
     id = models.AutoField(primary_key = True)
     code = models.CharField(max_length = 20)
     libelle = models.CharField(max_length = 255)
     date = models.DateTimeField(default=datetime.datetime.now)
     class Meta: 
      db_table = "Tab_com"

     def save(self, *args, **kwargs):
        # Update the date field to the current date and time
        self.date = datetime.datetime.now()
        super().save(*args, **kwargs) 

class Tab_banque(models.Model): 
     id = models.AutoField(primary_key = True)
     code = models.CharField(max_length = 20)
     libelle = models.CharField(max_length = 255)
     date = models.DateTimeField(default=datetime.datetime.now)
     class Meta: 
      db_table = "Tab_banque"

     def save(self, *args, **kwargs):
        # Update the date field to the current date and time
        self.date = datetime.datetime.now()
        super().save(*args, **kwargs)  

class Tab_coffre(models.Model): 
     id = models.AutoField(primary_key = True)
     code = models.CharField(max_length = 20)
     libelle = models.CharField(max_length = 255)
     date = models.DateTimeField(default=datetime.datetime.now)
     class Meta: 
      db_table = "Tab_coffre"

     def save(self, *args, **kwargs):
        # Update the date field to the current date and time
        self.date = datetime.datetime.now()
        super().save(*args, **kwargs)

