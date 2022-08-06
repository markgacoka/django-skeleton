from django.db import models
from django.utils.translation import gettext_lazy as _

class ExampleModel(models.Model):
    example_field = models.TextField(default='Text', max_length=256, unique=False, blank=True)

    class Meta:
        verbose_name = _('example_model')
        verbose_name_plural = _('example_models')
        db_table = 'example_models'
        abstract = False

    def __str__(self):
        return self.example_field
