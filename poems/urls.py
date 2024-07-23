# This file is where we'll list our poems app-specific URLs.

from django.urls import path
# from . import views
from .views import PoemList, poem_detail_ui, poem_list, poem_detail


urlpatterns = [
    # TODO
    path('', PoemList.as_view(), name='poems_list'), 
    path('poems/', PoemList.as_view(), name='poems_list'),
    
    path('poems/<int:id>/', poem_detail_ui, name='poem_detail_ui'),
    
    path('poems-api/', poem_list, name='poems'),
    path('poems-api/<int:id>/', poem_detail),
]
