from django.db import models


# Create your models here.
class Word(models.Model):
    size = models.IntegerField(null=False, default=0)
    word = models.CharField(null=False, max_length=6, unique=True)

    class Meta:
        ordering = ('word',)

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        word = str(self.word)
        self.size = len(word)
        super().save(*args, **kwargs)


class HiddenWord(models.Model):
    size = models.IntegerField(null=False, default=0)
    word = models.CharField(null=False, max_length=6, unique=True)

    class Meta:
        ordering = ('word',)

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        word = str(self.word)
        self.size = len(word)
        super().save(*args, **kwargs)
