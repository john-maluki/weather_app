from django.test import SimpleTestCase
from weather.forms import CityForm

class TestCityForm(SimpleTestCase):
    def test_form_is_valid(self):
        form = CityForm (data = {
            'name' : 'nairobi'
        })

        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form = CityForm (data = {})

        self.assertFalse(form.is_valid())
