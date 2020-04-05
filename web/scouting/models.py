from django.db import models

# Create your models here.


class YearSelection(models.Model):
    query_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Selection(models.Model):
    query = models.ForeignKey(YearSelection, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    answers = models.IntegerField(default=0)
