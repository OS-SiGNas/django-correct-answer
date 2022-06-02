from django.db import models
from django.db.models.fields import BooleanField, CharField

class Quiz(models.Model):
    name = CharField(
        max_length=20,
        null=False,
        unique=True,
        verbose_name='name'
    )
    description = CharField(max_length=250,null=True)
    def __str__(self):
        return '%s' %(self.name)

class Multiple(models.Model):
    title = CharField(max_length=250)
    correct = CharField(max_length=30)
    option_a = CharField(max_length=30)
    option_b = CharField(max_length=30)
    option_c = CharField(max_length=30)
    option_d = CharField(max_length=30)
    quiz = models.ForeignKey(
        Quiz,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return '%s' %(self.title)

class True_False(models.Model):
    title = CharField(max_length=250)
    correct = BooleanField()
    quiz = models.ForeignKey(
        Quiz,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return '%s' %(self.title)
