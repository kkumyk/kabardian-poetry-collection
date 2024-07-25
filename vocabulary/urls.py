from django.urls import path
from .views import VocabularyList, vocabulary_list, vocabulary_detail


urlpatterns = [
    path('vocabulary/', VocabularyList.as_view(), name='vocabulary-list'),
    path('vocabulary/api/', vocabulary_list, name='vocabulary-detail-list'),
    path('vocabulary/api/<int:id>/', vocabulary_detail, name='vocabulary-detail'),
]