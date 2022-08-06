from django.test import TestCase
from django.conf import settings
from .models import ExampleModel

class TestHomepage(TestCase):
    def test_debug_off(self):
        self.assertFalse(settings.DEBUG)

    def test_homepage(self):
        r = self.client.get('/', follow=True)
        self.assertEqual(r.status_code, 200)

class TestExampleModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.example_model = ExampleModel.objects.create(
            example_field = 'test_data',
        )

    def test_example_model_str(self):
        """ Tests the __str__ of the ExampleModel model"""
        self.assertEqual(str(self.example_model), 'test_data')

    def test_create_example_model(self):
        """ Tests that a field with text input can be created"""
        self.assertEqual(self.example_model.example_field, 'test_data')