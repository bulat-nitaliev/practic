from rest_framework.test import APITestCase
from general.factories import UserFactory, VredPrivichkiFactory
from rest_framework import status
from general.models import VredPrivichki
from datetime import datetime

class VredprivichkiTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = '/api/vredprivichki/'

    def test_list_vredprivichki(self):
        task = VredPrivichkiFactory.create_batch(15, user=self.user)
        VredPrivichkiFactory.create_batch(5)

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 10)
        self.assertEqual(response.data['count'], 15)

        self.assertEqual(VredPrivichki.objects.all().count(), 20)

    def test_list_structure(self):
        task = VredPrivichkiFactory(user=self.user)
        data =  {
            "son": task.son,
            "telefon": task.telefon,
            "haram": task.haram,
            "eda": task.eda,
            "created_at": str(task.created_at)
            }

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data['results'][0], data)

    def test_post_vredprivichki(self):
        data = {
            "son": True,
            "telefon": True,
            "haram": False,
            "eda": True
            }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        now = datetime.now()
        today = now.strftime('%Y-%m-%d')
        data["created_at"] = today

        self.assertDictEqual(response.data, data)

    def test_post_vredprivichki_unautorized(self):
        self.client.logout()
        data = {
            "son": True,
            "telefon": False,
            "haram": False,
            "eda": True
            }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_post_vredprivichki_from_user(self):
        data = {
            "son": True,
            "telefon": False,
            "haram": False,
            "eda": True
            }
        VredPrivichkiFactory.create_batch(5)
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(len(VredPrivichki.objects.filter(user=self.user)), 1)
        self.assertEqual(VredPrivichki.objects.all().count(), 6)

    def test_retrive_vredprivichki(self):
        task = VredPrivichkiFactory(user=self.user)

        data =  {
            "son": task.son,
            "telefon": task.telefon,
            "haram": task.haram,
            "eda": task.eda,
            "created_at": str(task.created_at)
            }

        response = self.client.get(f'{self.url}{task.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, data)

    def test_retrive_islam_not_main(self):
        task = VredPrivichkiFactory()
        VredPrivichkiFactory.create_batch(3,user=self.user)

        response = self.client.get(f'{self.url}{task.pk}/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Вы неможете посмотреть чужие дела')