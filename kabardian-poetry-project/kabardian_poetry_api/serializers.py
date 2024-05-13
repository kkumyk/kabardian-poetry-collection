from rest_framework import serializers
from .models import Poem, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'type', 'eng_transl', 'rus_transl', 'ipa']

class PoemSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True)

    class Meta:
        model = Poem
        fields = ['id', 'name', 'author', 'text', 'words']
        
    def create(self, validated_data):
        words_data = validated_data.pop('words')
        poem = Poem.objects.create(**validated_data)
        for word_data in words_data:
            word, _ = Word.objects.get_or_create(**word_data)
            poem.words.add(word)
        return poem