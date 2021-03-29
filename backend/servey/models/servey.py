from django.db import models

class Servey(models.Model):
    question_number = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=100)
    answer_01 = models.CharField(max_length=100)
    answer_02 = models.CharField(max_length=100)
    answer_03 = models.CharField(max_length=100)
    answer_04 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'servey'