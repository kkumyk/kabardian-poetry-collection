from django.test import TestCase, Client
from django.urls import reverse
from .models import Poem, Word
from django.shortcuts import get_list_or_404
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
            Poem.objects.create(title=f"Poem {i}", contents=f"Content {i}")
            
    def test_poems_list_view_status_code(self):
        response = self.client.get(reverse('poems_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_poems_list_view_template(self):
        response = self.client.get(reverse('poems_list'))
        self.assertTemplateUsed(response, 'poems/index.html')

    def test_poems_list_view_queryset(self):
        response = self.client.get(reverse('poems_list'))
        # test first page with three items
        poems = Poem.objects.all().order_by("title")[:21] # retrieve 21 objects from the database - testing first page with 21 poems
        # access the context data passed to the template by the view
        # object_list is the default context variable that contains the list of objects - poems, which is the context variable passed to the template by the view
        # the actual queryset - the list of objects from the view's context; the expected queryset you want to compare against
        # transform = lambda x :x the transform arguments is used to transform items in the query set before comparison
        # lambda x: x is an identity function, meaning no transformation was applied
        self.assertQuerySetEqual(response.context['object_list'], poems, transform = lambda x :x)

'''
- check if the view retrieves the correct poem and related words
- verify the correct template is used
- verify 404 error is raised for non-existing poem
'''

class PoemDetailUiViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.poem = Poem.objects.create(title="Sample Poem", contents= "Amazing Verses")
        
        # create words associated with the poem
        for i in range(3):
            Word.objects.create(poem=self.poem, word=f"Word {i}")
    
    def test_poem_detail_ui_view_status_code(self):
        response = self.client.get(reverse("poem_detail_ui", args=[self.poem.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_poem_detail_ui_view_template(self):
        response = self.client.get(reverse("poem_detail_ui", args=[self.poem.id]))
        self.assertTemplateUsed(response, "poems/poem_detail.html")
    
    def test_poem_detail_ui_view_context(self):
        response = self.client.get(reverse("poem_detail_ui", args=[self.poem.id]))
        self.assertEqual(response.context['poem'], self.poem)
        self.assertQuerySetEqual(response.context['words'], Word.objects.filter(poem=self.poem), transform = lambda x: x)
    
    def test_poem_detail_ui_view_404(self):
        response = self.client.get(reverse("poem_detail_ui", args=[999])) # assuming that there is no poem with the id of 999
        self.assertEqual(response.status_code, 404)