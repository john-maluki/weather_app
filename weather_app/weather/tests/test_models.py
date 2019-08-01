from django.test import TestCase
from django.urls import reverse



from weather.models import City
from weather.forms import CityForm

class CityTests(TestCase):
    def setUp(self):
        City.objects.create(name='kisumu')
    
    def test_name_content(self):
        post = City.objects.get(id=1)
        expected_object_name = f'{post.name}'

        self.assertEqual(expected_object_name, 'kisumu')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'kisumu')
        self.assertTemplateUsed(response, 'weather/weather.html')    

       
