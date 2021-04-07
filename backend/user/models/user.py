from django.db import models


class User(models.Model):
    user_number = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    survey = models.IntegerField(default=0, blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
