# This file is where we'll list our poems app-specific URLs.

from . import views
from django.urls import path

urlpatterns = [
    path('poems/', views.PoemList.as_view(), name='poems_list'),
    path('poems/<int:id>/', views.poem_detail_ui, name='poem_detail_ui'),
    path('poems-api/', views.poem_list, name='poems'),
    path('poems-api/<int:id>/', views.poem_detail),
]