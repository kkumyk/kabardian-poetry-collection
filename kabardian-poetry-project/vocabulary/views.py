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
@api_view(['GET', 'POST'])
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get and delete a word from a vocabulary list:
@api_view(['GET', 'DELETE'])
def vocabulary_detail(request, id):
    try:
        word = Vocabulary.objects.get(id=id)
    except Vocabulary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VocabularySerializer(word)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)