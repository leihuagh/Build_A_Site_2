from django.db import models
from core.models import TimeStampModel
from ._question import Question


class Choice(TimeStampModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    def choice_question(self):
        return self.question.votes
