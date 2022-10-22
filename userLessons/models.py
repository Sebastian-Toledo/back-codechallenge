from asyncio.windows_events import NULL
from email.policy import default
from enum import unique
from random import choices
from secrets import choice
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User (models.Model):
    username    = models.CharField(max_length = 20, unique = True )
    friends     = models.ManyToManyField('User',blank = True)

    def __str__(self):
        return self.username

lessonName = [
    ('MA' , 'Math'),
    ('SP', 'Spanish'),
    ('GT', 'Guitar'),
]

class Lesson (models.Model):
    name    = models.CharField(max_length = 2, choices = lessonName, default= 'MA')
    classesPerWeek = models.IntegerField(validators=[ MaxValueValidator(7),MinValueValidator(1)], default = 1, blank = False)
    user = models.ForeignKey('User', on_delete = models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.user.username + ' cantidad clases ' + str(self.classesPerWeek)