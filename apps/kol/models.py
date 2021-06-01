from django.db import models


# Create your models here.
from import_export.resources import ModelResource


class Kol(models.Model):

    class Specialty(models.TextChoices):
        oncology = 'oncology', 'Oncology'
        second = 'second', 'Second'
        third = 'third', 'Third'

    first_name = models.CharField(
        max_length=255,
    )
    middle_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    credential = models.CharField(
        max_length=255,
    )
    specialty = models.CharField(
        max_length=255,
        choices=Specialty.choices,
    )

    def full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}, ' \
               f'{self.credential}'

    @classmethod
    def export_resource_classes(cls):
        return {
            'kol': ("Kol resource", KolResource)
        }


class KolResource(ModelResource):
    class Meta:
        model = Kol
