# from django.http import JsonResponse
# from .models import Poem, Word
# from .serializers import PoemSerializer

from rest_framework import generics
from .models import Poem
from .serializers import PoemSerializer

# def poem_list(request):
#     poems = Poem.objects.all()
#     serializer =  PoemSerializer(poems, many=True)
#     return JsonResponse(serializer.data, safe=False)


class PoemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer

class PoemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer