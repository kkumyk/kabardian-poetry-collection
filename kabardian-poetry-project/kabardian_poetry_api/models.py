from django.db import models

class Word(models.Model):
        word = models.CharField(max_length=100)
        type = models.CharField(max_length=100)
        eng_transl = models.CharField(max_length=100)
        rus_transl = models.CharField(max_length=100)
        ipa = models.CharField(max_length=100)
        
        def __str__(self):
            return self.eng_transl


class Poem(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    text = models.TextField()
    words = models.ManyToManyField(Word)
    
    def __str__(self):
        return self.title
    



# SELECT * FROM kabardian_poetry_api_poem p
# JOIN kabardian_poetry_api_poem_words pw on pw.poem_id = p.id
# JOIN kabardian_poetry_api_word w on w.id = pw.word_id;
