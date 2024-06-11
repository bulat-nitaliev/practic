from rest_framework.test import APITestCase
from general.factories import UserFactory, CelFactory, CommentFactory
from rest_framework import status
from general.models import User, Cel
from django.contrib.auth.hashers import check_password
from datetime import datetime, date

class CelTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = '/api/cel/'

    def test_list_cel(self):
        CelFactory.create_batch(15, author=self.user)

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 15)
        self.assertEqual(len(response.data['results']), 10)

    def test_cel_structure(self):
        cel = CelFactory(author=self.user)
        response = self.client.get(self.url, format='json')

        data = {
            'id': cel.id,
            'name': cel.name,
            'comment': '',
            'dt_beg': str(cel.dt_beg),
            'dt_end': str(cel.dt_end)
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data['results'][0], data)


    def test_cel_comment_structure(self):
        cel = CelFactory(author=self.user)
        comments = CommentFactory.create_batch(5,author=self.user, cel=cel)
        response = self.client.get(self.url, format='json')

        data = {
            'id': cel.id,
            'name': cel.name,
            'comment': [i.body for i in comments],
            'dt_beg': str(cel.dt_beg),
            'dt_end': str(cel.dt_end)
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data['results'][0], data)


    def test_cel_create(self):
        data = {"name": "New Cel"}
        response = self.client.post(self.url, data=data, format="json")

        now = datetime.now()
        today = now.strftime('%Y-%m-%d')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        res = {"name": data["name"], "dt_beg": today}
        self.assertDictEqual(res, response.data)

        cel = Cel.objects.last()
        self.assertEqual(cel.author, self.user)
        self.assertEqual(cel.name, data["name"])


    def test_unauthorized_cel_request(self):
        self.client.logout()
        data = {"name": "New Cel"}
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Cel.objects.all().count(), 0)

    def test_retrieve_cel(self):
        cel = CelFactory(author=self.user)

        response = self.client.get(f'{self.url}{cel.pk}/', format='json')
        data = {
            'id': cel.id,
            'name': cel.name,
            'comment': '',
            'dt_beg': str(cel.dt_beg),
            'dt_end': str(cel.dt_end)
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(data, response.data)


    def test_retrieve_not_mine_cel(self):
        cel = CelFactory()

        response = self.client.get(f'{self.url}{cel.pk}/', format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_put_cel(self):
        cel = CelFactory(author=self.user, name="old cel")
        data = {"name": "Put cel"}

        response = self.client.put(f'{self.url}{cel.pk}/', data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['name'], response.data['name'])
        cel.refresh_from_db()

        self.assertEqual(cel.name, data['name'])


    def test_put_cel_structure(self):
        cel = CelFactory(author=self.user, name="old cel")
        data = {"name": "Put New cel"}

        response = self.client.put(f'{self.url}{cel.pk}/', data=data, format='json')

        data_res = {
            'name': data['name'],
            'comment': '',
            'dt_beg': str(cel.dt_beg),
            'dt_end': str(cel.dt_end)
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, data_res)

    def test_delete_cel(self):

        cels = CelFactory.create_batch(5, author=self.user)
        cel = CelFactory(author=self.user)

        self.assertEqual(Cel.objects.filter(author=self.user).count(), 6)
        response = self.client.delete(f'{self.url}{cel.pk}/', format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cel.objects.all().count(), 5)

    def test_delete_not_main_cel(self):

        cels = CelFactory.create_batch(5)
        cel = CelFactory()

        self.assertEqual(Cel.objects.filter(author=self.user).count(), 0)
        response = self.client.delete(f'{self.url}{cel.pk}/', format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)





