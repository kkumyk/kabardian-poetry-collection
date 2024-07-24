from rest_framework import serializers
from .models import Poem, Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'eng_transl', 'rus_transl']

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ['id', 'title', 'author', 'contents']