from django.contrib import admin
from .models import Poem, Word

admin.site.register(Poem)
admin.site.register(Word)