from django.db import models
from user.models import User
from owner.models import Owner
from facilities.models import Facilities
from event.models import Event
# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(db_column='Booking_id', primary_key=True)  # Field name made lowercase.
    # user_id = models.IntegerField(blank=True, null=
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    # em_id = models.IntegerField(blank=True, null=True)
    em = models.ForeignKey(Owner, on_delete=models.CASCADE)
    # facility_id = models.IntegerField(blank=True, null=True)
    facility = models.ForeignKey(Facilities, on_delete=models.CASCADE)
    amount = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()
    status = models.CharField(max_length=45)
    # event_id = models.IntegerField()
    event=models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'booking'

