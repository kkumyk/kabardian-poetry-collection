from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField


class Word(models.Model):
        word = models.CharField(max_length=100)
        type = models.CharField(max_length=100, default='noun')
        eng_transl = models.CharField(max_length=100)
        rus_transl = models.CharField(max_length=100)
        ipa = models.CharField(max_length=100)
        # audio_url = models.URLField(max_length=100)
        
        def __str__(self):
            return self.eng_transl
                    
                    
# class Vocabulary(models.Model):
#     type = models.CharField(max_length=100, default='nouns')
#     words = models.ManyToManyField(Word, related_name='vocabulary_words')

class Poem(models.Model):
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    # audio_url = models.URLField(max_length=300)
    text = models.TextField()
    vocabulary = models.ForeignKey(Word, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name