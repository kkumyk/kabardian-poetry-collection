from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Word, Poem
from .serializers import WordSerializer, PoemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
import logging

# Set up logging
logger = logging.getLogger(__name__)

# the generic.ListView class will display all poems
class PoemList(generic.ListView):
    queryset = Poem.objects.all().order_by("title")
    template_name = "poems/index.html"
    paginate_by = 21
    
# the view for a single poem displayed on UI
def poem_detail_ui(request, id):
    poem = get_object_or_404(Poem, id=id)
    
    words = Word.objects.filter(poem=poem)
    context = {"poem": poem, "words": words}
    
    return render(
        request,
        "poems/poem_detail.html",
        context
    )
    
@login_required
@api_view(['GET', 'POST'])
def poems_list_api_view(request):
    '''
    This view allows a logged-in user to see poems collection.
    The superuser can also add a new poem.
    '''
    if request.method == 'GET':
        poems = Poem.objects.all()
        serializer =  PoemSerializer(poems, many=True)
        return Response({'poems': serializer.data})

    if request.method == 'POST' and request.user.is_superuser:
        serializer = PoemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# get/update/delete a single poem
@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def poem_detail_api_view(request, id):
    '''
    This view allows a logged-in superuser to view, update and delete a single poem.
    '''
    if request.user.is_superuser:
        # check if it is a valid request
        try:
            poem = Poem.objects.get(pk=id)
        except Poem.DoesNotExist:
            logger.debug(f"Poem with id {id} does not exist.")
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
            return Response(data) # return the combined data as JSON response

        # update title, author and test fields of a singular poem
        elif request.method == 'PUT':
            serializer = PoemSerializer(poem, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.debug(f"PUT request data is invalid: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
        elif request.method == 'DELETE':
            poem.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
# get a list of all words; add a new word:
@login_required
@api_view(['GET', 'POST'])
def word_list(request):
    if request.method == 'GET':
        words = Word.objects.all()
        serializer =  WordSerializer(words, many=True)
        return Response({'words': serializer.data})

    if request.method == 'POST' and request.user.is_superuser:
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# get, update and delete a single word; restricted to superusers only:
@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def word_detail(request, id):
    
    if request.user.is_superuser:
        # check for a valid request
        try: 
            word = Word.objects.get(pk=id)
        except Word.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # get the word instance or return a 404 response if not found
        
        if request.method == 'GET':
            word_serializer = WordSerializer(word) # serialize the word instance
            data = word_serializer.data
            return Response(data)

        # update fields of a word
        elif request.method == 'PUT':
            serializer = WordSerializer(word, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
        elif request.method == 'DELETE':
            word.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)