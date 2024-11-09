from django.db import models


# Create your models here.
class Word(models.Model):
    size = models.IntegerField(null=False)
    word = models.CharField(null=False, max_length=6)

    def __str__(self):
        return self.word
