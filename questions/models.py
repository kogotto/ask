from django.db import models

class Question(models.Model):
    text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.text
