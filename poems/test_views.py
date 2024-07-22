from django.test import TestCase, Client
from django.urls import reverse
from .models import Poem, Word

'''
testing generic list view PoemList:
    - check if the view retrieves all poems by title
    - verify if the correct template is used
    - test if pagination works as expected
    
To validate the view behavior the Django test Client is used. This class acts as a dummy web browser that can be used to simulate GET and POST requests on a URL and observe the response.
Almost everything about the response can be seen:
    - low level HTTP (result headers and status codes)
    - the template used to render HTML
    - the context data passed to the template
    - redirect chains if any with URL status code at each step
The above allows to verify the view acts as expected. 
'''

class PoemListViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # creating 30 poems for testing pagination
        for i in range(30):
            Poem.objects.create(title=f"Poem {i}", content=f"Content {i}")
            
            
    def test_poem_list_view_status_code(self):
        response = self.client.get(reverse('poem_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_poem_list_view_template(self):
        response = self.client.get(reverse('poem_list'))
        self.assertTemplateUsed(response, 'poems/index.html')

    def test_poem_list_view_queryset(self):
        response = self.client.get(reverse('poem_list'))
        # test first page with three items
        poems = Poem.objects.all().order_by("title")[:3] # retrieve three objects from the database
        # access the context data passed to the template by the view
        # object_list is the default context variable that contains the list of objects - poems, which is the context variable passed to the template by the view
        # the actual queryset - the list of objects from the view's context, the expected queryset you want to compare against
        self.assertQuerySetEqual(response.context['object_list'], poems, transform = lambda x :x) 







'''
- check if the view retrieves the correct poem and related words
- verify the correct template is used
- verify 404 error is raised for non-existing poem
'''