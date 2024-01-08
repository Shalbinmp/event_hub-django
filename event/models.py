from django.db import models
from owner.models import Owner

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    image = models.CharField(max_length=500)
    # em_id = models.IntegerField()
    em = models.ForeignKey(Owner, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'event'

