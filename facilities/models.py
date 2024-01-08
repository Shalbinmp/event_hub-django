from django.db import models
from owner.models import Owner
from event.models import Event
# Create your models here.
class Facilities(models.Model):
    facility_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    # em_id = models.IntegerField(blank=True, null=True)
    em=models.ForeignKey(Owner, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, null=True)
    # event_id = models.IntegerField(blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'facilities'
