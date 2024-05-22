from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Vocabulary
from .serializers import VocabularySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from poems.models import Word


class VocabularyList(generic.ListView): 
    queryset = Vocabulary.objects.all()
    template_name = "vocabulary/vocabulary.html"

    
# retrieve and add to a vocabulary list:
@api_view(['GET', 'POST', 'DELETE'])
def vocabulary_list(request):
    
    if request.method == 'GET':
        words = Vocabulary.objects.all()
        serializer =  VocabularySerializer(words, many=True)
        return Response({'vocabulary': serializer.data})
        
    if request.method == 'POST':
        # TODO check if the word is already in the user's vocabulary
        serializer = VocabularySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
# delete a word from a vocabulary list:

@api_view(['DELETE'])
def vocabulary_detail(request, id):
    try:
        vocabulary_entry = Vocabulary.objects.get(word_id=id)
        
    except Vocabulary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        
        serializer = VocabularySerializer(vocabulary_entry, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        vocabulary_entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)