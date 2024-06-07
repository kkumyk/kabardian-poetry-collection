from django.db import models
from django.contrib.auth.models import User
from poems.models import Word


class Vocabulary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted, their vocabulary entries are also deleted;
    word = models.ForeignKey(Word, on_delete=models.CASCADE) # if a word is deleted, the corresponding vocabulary entries are also deleted

    class Meta:
        unique_together = ('user', 'word') # the same word cannot be added multiple times to the same user's vocabulary;

    def __str__(self):
        return f"{self.word.word}" # {self.user.username} - 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    