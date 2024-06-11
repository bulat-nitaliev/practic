import factory
from factory.django import DjangoModelFactory
from general.models import User, Islam, VredPrivichki, Cel, Comment


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = True

class IslamFactory(DjangoModelFactory):
    class Meta:
        model = Islam

    quran = factory.Faker('pyint', min_value=0, max_value=1000)
    solat_duha = factory.Faker('pybool')
    solat_vitr = factory.Faker('pybool')
    mechet_fard = factory.Faker('pyint', min_value=0, max_value=5)
    tauba = factory.Faker('pybool')
    sadaka = factory.Faker('pybool')
    zikr_ut = factory.Faker('pybool')
    zikr_vech = factory.Faker('pybool')
    rodstven_otn = factory.Faker('pybool')
    created_at = factory.Faker('date_object')
    user = factory.SubFactory(UserFactory)

class VredPrivichkiFactory(DjangoModelFactory):
    class Meta:
        model = VredPrivichki

    son = factory.Faker('pybool')
    telefon = factory.Faker('pyint', min_value=0, max_value=1000)
    haram = factory.Faker('pybool')
    eda = factory.Faker('pybool')
    created_at = factory.Faker('date_object')
    user = factory.SubFactory(UserFactory)

class CelFactory(DjangoModelFactory):
    class Meta:
        model = Cel

    author = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    dt_beg = factory.Faker('date_object')
    dt_end = factory.Faker('date_object')

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    body = factory.Faker('text')
    author = factory.SubFactory(UserFactory)
    cel = factory.SubFactory(CelFactory)
    created_at = factory.Faker('date_object')