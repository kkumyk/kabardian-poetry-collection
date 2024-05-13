from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

class Vocabulary(models.Model):
    
    class Word(models.Model):
        word = models.CharField(max_length=100)
        eng_transl = models.CharField(max_length=100)
        kab_transl = models.CharField(max_length=100)
        ipa = models.CharField(max_length=100)
        audio_url = models.URLField(max_length=100)
    
    words = models.ManyToManyField(Word, related_name='vocabulary_words')


class Poem(models.Model):
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    audio_url = models.URLField(max_length=300)
    text = models.TextField()
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)