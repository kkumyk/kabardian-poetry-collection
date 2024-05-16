from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
        word = models.CharField(max_length=100, unique=True)
        type = models.CharField(max_length=100)
        eng_transl = models.CharField(max_length=100)
        rus_transl = models.CharField(max_length=100)
        ipa = models.CharField(max_length=100)
        
        def __str__(self):
            return self.eng_transl


class Poem(models.Model):
    title = models.CharField(max_length=300, unique=True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    words = models.ManyToManyField(Word)
    
    def __str__(self):
        return self.title
    



# SELECT * FROM poems_poem p
# JOIN poems_poem_words pw on pw.poem_id = p.id
# JOIN poems_word w on w.id = pw.word_id;