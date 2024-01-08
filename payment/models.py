from django.db import models
from user.models import User
from booking.models import Booking
from owner.models import Owner

# Create your models here.

class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    # booking_id = models.IntegerField()
    booking =models.ForeignKey(Booking, on_delete=models.CASCADE)
    # user_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=45)
    cvv = models.CharField(max_length=45)
    account_no = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    amount = models.CharField(max_length=45)
    # em_id = models.IntegerField(blank=True, null=True)
    em = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment'

