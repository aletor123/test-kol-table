import factory

from apps.kol.models import Kol


class KolsFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    middle_name = factory.Faker('last_name')
    last_name = factory.Faker('last_name')
    credential = factory.Faker('suffix')
    specialty = factory.Faker('bs')

    class Meta:
        model = Kol
