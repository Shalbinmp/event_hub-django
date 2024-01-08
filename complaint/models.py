from django.db import models
from user.models import User
from owner.models import Owner

# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    reply = models.CharField(max_length=45)
    # user_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # em_id = models.IntegerField(blank=True, null=True)
    em = models.ForeignKey(Owner, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'complaint'

