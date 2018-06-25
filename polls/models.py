from django.db import models

import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 5 return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # 5 Fix the code
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        # 5 Now the test will pass

        # 5 Add further tests to polls/tests.py


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text