from django.urls import reverse, resolve
from django.test import SimpleTestCase
from weather.views import index, delete_city



class TestUrls(SimpleTestCase):
    def test_delete_url_is_resolved(self):
        url = reverse('delete_city', args= ['city_name'])
        self.assertEqual(resolve(url).func, delete_city)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)
#     # def test_home_url(self):
#     #     path = reverse('home')
#     #     assert resolve(path).view_name == 'home'
#     # def test_delete_city_url(self):
#     #     path = reverse('delete_city', kwargs= {'city_name' : str})
#     #     assert resolve(path).view_name == 'delete_city'  
#        