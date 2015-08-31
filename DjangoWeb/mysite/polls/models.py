from django.db import models
import _datetime


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= _datetime.timezone.now() - _datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Version(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
