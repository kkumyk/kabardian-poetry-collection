from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Vocabulary
from .serializers import VocabularySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class VocabularyList(generic.ListView): 
    queryset = Vocabulary.objects.all()
    template_name = "vocabulary/vocabulary.html"
    
    

@api_view(['GET', 'POST'])

def vocabulary_list(request):
    
    if request.method == 'GET':

        words = Vocabulary.objects.all()
        serializer =  VocabularySerializer(words, many=True)

        return Response({'words': serializer.data})

    if request.method == 'POST':
        # TODO check if the word is already in the user's vocabulary
        # word = Word.objects.get_or_create(text=word)
        # vocabulary_entry = Vocabulary.objects.get_or_create(word=word)
        
        serializer = VocabularySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)