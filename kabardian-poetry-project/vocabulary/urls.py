from . import views
from django.urls import path

urlpatterns = [
    path('vocabulary/', views.VocabularyList.as_view(), name='vocabulary-list'),
    path('vocabulary-api/<int:id>/', views.vocabulary_detail, name='vocabulary-detail'),
]