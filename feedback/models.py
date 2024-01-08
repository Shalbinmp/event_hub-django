from django.db import models
from owner.models import Owner
from user.models import User

# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=45)
    # user_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # em_id = models.IntegerField(blank=True, null=True)
    em = models.ForeignKey(Owner, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'feedback'
