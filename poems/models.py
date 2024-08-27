from django.db import models

class Word(models.Model):
        id = models.AutoField(primary_key=True, db_column='word_id')
        word = models.TextField()
        eng_transl = models.TextField()
        rus_transl = models.TextField()
        
        def __str__(self):
            return self.eng_transl


class Poem(models.Model):
    id = models.AutoField(primary_key=True, db_column='poem_id')
    title = models.TextField()
    author = models.TextField()
    contents = models.TextField()
    words = models.ManyToManyField(Word)
    
    def __str__(self):
        return self.title

# The __str__() dunder method lets you represent your class object as a string for the benefit of your app's user.