from weather.views import index, delete_city
from django.test import RequestFactory, TestCase, Client
from django.http import HttpRequest

import json
from django.urls import reverse
# from mixer.backend.django import mixer
from weather.models import City
import pytest

# @pytest.mark.django_db
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse('home')
        self.delete_city = reverse('delete_city', args= ['mombasa'])
        self.poject = City.objects.create(
            name = 'mombasa'
        )
        

    def test_index_get(self):
        response = self.client.get(self.home, {
            'name' : 'mombasa'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/weather.html')

    def test_index_get_ne(self):
        response = self.client.get(self.home, {
            'name' : 'h'
        })
        self.assertEqual(response.status_code, 200)
           
        

    def test_index_post(self):
        response = self.client.post(self.home, {
            'name' : 'kiambu'
        })

        response_already_in_database = self.client.post(self.home, {
            'name' : 'kiambu'
        })
        
        self.assertEqual(response_already_in_database.status_code, 200)
        self.assertEqual(response.status_code, 200)


    def test_index_post_ne(self):
        response = self.client.post(self.home, {
            'name' : 'h'
        })
        self.assertEqual(response.status_code, 200)    
        

    def test_delete_city(self):
        city = City.objects.create(name = 'mumbai')
        response = self.client.delete(self.delete_city, json.dumps({
            'id' : 1
        }))

        self.assertEqual(response.status_code, 302) 


    # def test_view_variable(self, variables):
    #     assert variables[''] == 'bar'
    #     assert variables.get('bar') == 'foo'
    #     assert variables.get('missing') is None     
        


    # def test_delete_city_post(self):
    #     response = self.client.delete(self.delete_city)
    #     self.assertEqual(response.status_code, 200)
             


         
              


    # def test_index(self):
    #     self.assertTemplateUsed('weather/weather.html')


    # # def test_delet_city(self):
    # #     city_name = 'name'
    # #     City.objects.create(name=city_name)
    # #     t = City.objects.get(name=city_name).delete()   

    #     self.assertTrue(t)

    # def test_home_page_status_code(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)

    # def test_home_url_by_name(self):
    #     response = self.client.post(reverse('home'))
    #     self.assertEqual(response.status_code, 200)
    # 
    # def test_home_url_by_name(self):
    #     City.objects.create(name= 'sample')
    #     response = self.client.post(reverse('home'))
    #     self.assertEqual(response.status_code, 200)  

    
 
    # def test_delete_url_by_name(self):
    #     response = self.client.delete(reverse('delete_city', kwargs= ['nairobi']))
    #     self.assertEqual(response.status_code, 200)        

      

        

        