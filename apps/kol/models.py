from django.db import models


# Create your models here.

class Kol(models.Model):

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
    )

    def full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}, ' \
               f'{self.credential}'
