from django.db import models

# Create your models here.
class Owner(models.Model):
    em_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    emailid = models.CharField(max_length=45)
    license = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    image = models.CharField(max_length=500)



    class Meta:
        managed = False
        db_table = 'owner'


