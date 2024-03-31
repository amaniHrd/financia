from django.db import models

# Create your models here.
# try to understand in a deep way what's a model and what's its utility 
class Tab_aux(models.Model):
    id = models.AutoField(primary_key = True)
    code = models.CharField(max_length = 20)
    libelle = models.CharField(max_length = 255)
    class Meta: 
     db_table = "Tab_aux"

class Tab_com(models.Model): 
     id = models.AutoField(primary_key = True)
     code = models.CharField(max_length = 20)
     libelle = models.CharField(max_length = 255)
     class Meta: 
      db_table = "Tab_com"

class Tab_banque(models.Model): 
     id = models.AutoField(primary_key = True)
     code = models.CharField(max_length = 20)
     libelle = models.CharField(max_length = 255)
     class Meta: 
      db_table = "Tab_banque"



