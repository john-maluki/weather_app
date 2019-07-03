from django.apps import AppConfig
from weather.apps import WeatherConfig
from django.test import TestCase


class TestApp(TestCase):
    def test_app_name(self):
        app_name = WeatherConfig.name
        self.assertEqual(app_name, 'weather')