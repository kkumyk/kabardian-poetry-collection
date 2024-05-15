from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Word, Poem
from .serializers import WordSerializer, PoemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# get a GET request to return all existing poems in the db:

@api_view(['GET', 'POST'])
def poem_list(request):
    if request.method == 'GET':
        poems = Poem.objects.all()
        serializer =  PoemSerializer(poems, many=True)
        return JsonResponse({'poems': serializer.data})

    if request.method == 'POST':
        serializer = PoemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



# get a GET request to return a poem by id and include poems' words:
def poem_detail(request, id):
    # get the poem instance or return a 404 response if not found
    poem = get_object_or_404(Poem, pk=id)
    
    # serialize the poem instance
    poem_serializer = PoemSerializer(poem)
    
    # Get poem's words
    words = Word.objects.filter(poem=poem)
    
    # serialize poem's words
    word_serializer = WordSerializer(words, many=True)
    
    # combine poem data and words data into a single dictionary
    data = {
        'poem': poem_serializer.data,
        'words': word_serializer.data
    }
    
    # return the combined data as JSON response
    return JsonResponse(data)