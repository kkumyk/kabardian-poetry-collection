from django.db import models

class Word(models.Model):
        word = models.CharField(max_length=200, unique=True)
        eng_transl = models.CharField(max_length=1000)
        rus_transl = models.CharField(max_length=1000)
        ipa = models.CharField(max_length=100)
        
        def __str__(self):
            return self.eng_transl


class Poem(models.Model):
    title = models.CharField(max_length=300, unique=True)
    author = models.CharField(max_length=200)
    contents = models.TextField()
    words = models.ManyToManyField(Word)
    
    def __str__(self):
        return self.title
    
# The __str__() dunder method lets you represent your class object as a string for the benefit of your app's user.

# SELECT * FROM poems_poem p
# JOIN poems_poem_words pw on pw.poem_id = p.id
# JOIN poems_word w on w.id = pw.word_id;