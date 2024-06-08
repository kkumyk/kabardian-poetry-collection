from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Vocabulary
from .serializers import VocabularySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

    
# LoginRequiredMixin ensures that only authenticated users can access the view.
# If the user is not logged in, they will be redirected to the login page.

class VocabularyList(LoginRequiredMixin, generic.ListView):
    template_name = "vocabulary/vocabulary.html"
    
    # use a variable vocabulary_list which holds a list of Vocabulary objects to pass these to the template
    context_object_name = "vocabulary_list"
    
    def get_queryset(self):
        # filter the Vocabulary objects by the logged-in user
        return Vocabulary.objects.filter(user=self.request.user)


# retrieve and add to a vocabulary list
@login_required
@api_view(['GET', 'POST'])
def vocabulary_list(request):
    
    if request.method == 'GET':
        words = Vocabulary.objects.all()
        serializer = VocabularySerializer(words, many=True)
        return Response({'vocabulary': serializer.data})
        
    if request.method == 'POST':
        serializer = VocabularySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get and delete a word from a vocabulary list
@login_required
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