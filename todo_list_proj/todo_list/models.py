import datetime
from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField('What I have to do?', max_length=100)
    content = models.TextField('Details', blank=True)
    deadline = models.DateField('Deadline', default=datetime.date.today)

    def __str__(self):
        return self.title