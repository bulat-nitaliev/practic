from rest_framework.test import APITestCase
from general.factories import UserFactory, IslamFactory
from rest_framework import status
from general.models import Islam
from datetime import datetime

class IslamTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = '/api/islam/'

    def test_list_islam(self):
        task = IslamFactory.create_batch(15, user=self.user)
        IslamFactory.create_batch(5)

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 10)
        self.assertEqual(response.data['count'], 15)

        self.assertEqual(Islam.objects.all().count(), 20)

    def test_list_structure(self):
        task = IslamFactory(user=self.user)
        data = {
            "id": task.id,
            "quran": task.quran,
            "solat_duha": task.solat_duha,
            "solat_vitr": task.solat_vitr,
            "fadjr": task.fadjr,
            "mechet_fard": task.mechet_fard,
            "tauba": task.tauba,
            "sadaka": task.sadaka,
            "zikr_ut": task.zikr_ut,
            "zikr_vech": task.zikr_vech,
            "rodstven_otn": task.rodstven_otn,
            "created_at": str(task.created_at)
            }

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data['results'][0], data)

    def test_post_islam(self):
        data = {
            "quran": 10,
            "solat_duha": True,
            "solat_vitr": False,
            "fadjr": False,
            "mechet_fard": False,
            "tauba": True,
            "sadaka": False,
            "zikr_ut": False,
            "zikr_vech": False,
            "rodstven_otn": False
            }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        now = datetime.now()
        today = now.strftime('%Y-%m-%d')
        data["created_at"] = today

        self.assertDictEqual(response.data, data)

    def test_post_islam_unautorized(self):
        self.client.logout()
        data = {
            "quran": 10,
            "solat_duha": True,
            "solat_vitr": False,
            "fadjr": False,
            "mechet_fard": False,
            "tauba": True,
            "sadaka": False,
            "zikr_ut": False,
            "zikr_vech": False,
            "rodstven_otn": False
            }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_post_islam_from_user(self):
        data = {
            "quran": 10,
            "solat_duha": True,
            "solat_vitr": False,
            "fadjr": False,
            "mechet_fard": False,
            "tauba": True,
            "sadaka": False,
            "zikr_ut": False,
            "zikr_vech": False,
            "rodstven_otn": False
            }
        IslamFactory.create_batch(5)
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(len(Islam.objects.filter(user=self.user)), 1)
        self.assertEqual(Islam.objects.all().count(), 6)

    def test_retrive_islam(self):
        task = IslamFactory(user=self.user)

        data =  {
            "id": task.id,
            "quran": task.quran,
            "solat_duha": task.solat_duha,
            "solat_vitr": task.solat_vitr,
            "fadjr": task.fadjr,
            "mechet_fard": task.mechet_fard,
            "tauba": task.tauba,
            "sadaka": task.sadaka,
            "zikr_ut": task.zikr_ut,
            "zikr_vech": task.zikr_vech,
            "rodstven_otn": task.rodstven_otn,
            "created_at": str(task.created_at)
            }

        response = self.client.get(f'{self.url}{task.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, data)

    def test_retrive_islam_not_main(self):
        task = IslamFactory()
        IslamFactory.create_batch(3,user=self.user)



        response = self.client.get(f'{self.url}{task.pk}/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Вы неможете посмотреть чужие дела')

