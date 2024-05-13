from django.contrib import admin
from .models import Poem, Vocabulary, Word

admin.site.register(Poem)
admin.site.register(Vocabulary)
admin.site.register(Word)