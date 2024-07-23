# This file is where we'll list our poems app-specific URLs.

from django.urls import path
# from . import views
from .views import PoemList, poem_detail_ui, poems_list_api, poem_detail


urlpatterns = [
    
    # UI URL paths:
    path('', PoemList.as_view(), name='poems_list'), # TODO
    path('poems/', PoemList.as_view(), name='poems_list'), # TODO
    path('poems/<int:id>/', poem_detail_ui, name='poem_detail_ui'),
    
    # API URL paths:
    # path('poems-api/', poem_list, name='poems'),
    path('poems-api/', poems_list_api, name='poems_list_api'),
    
    path('poems-api/<int:id>/', poem_detail),
    
]
