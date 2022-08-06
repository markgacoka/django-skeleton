from django.test import TestCase
from .models import ExampleModel

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