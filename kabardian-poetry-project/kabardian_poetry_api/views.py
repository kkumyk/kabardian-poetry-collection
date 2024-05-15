from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Word, Poem
from .serializers import WordSerializer, PoemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def poem_list(request):
    if request.method == 'GET':
        poems = Poem.objects.all()
        serializer =  PoemSerializer(poems, many=True)
        return Response({'poems': serializer.data})

    if request.method == 'POST':
        serializer = PoemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def poem_detail(request, id):
    
    # check if it is a valid request
    try:
        poem = Poem.objects.get(pk=id)
    except Poem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) # get the poem instance or return a 404 response if not found
    
    if request.method == 'GET':
        poem_serializer = PoemSerializer(poem) # serialize the poem instance
        
        words = Word.objects.filter(poem=poem) # get poem's words
        word_serializer = WordSerializer(words, many=True) # serialize poem's words
        
        # combine poem data and words data into a single dictionary
        data = {
            'poem': poem_serializer.data,
            'words': word_serializer.data
        }
        
        # return the combined data as JSON response
        return Response(data)

    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass