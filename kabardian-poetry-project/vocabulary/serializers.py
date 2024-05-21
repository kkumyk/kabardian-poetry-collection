from rest_framework import serializers
from .models import Vocabulary


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['user_id', 'word_id']