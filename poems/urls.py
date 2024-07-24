# This file is where we'll list our poems app-specific URLs.

from django.urls import path
from .views import PoemList, poem_detail_ui, poems_list_api_view, poem_detail_api_view


urlpatterns = [
    path('', PoemList.as_view(), name='poems_list'), # TODO
    path('poems/', PoemList.as_view(), name='poems_list'), # TODO
    path('poems/<int:id>/', poem_detail_ui, name='poem_detail_ui'),
    path('poems/api/', poems_list_api_view, name='poems_list_api_view'),
    path('poems/api/<int:id>/', poem_detail_api_view, name='poems_detail_api_view')
]