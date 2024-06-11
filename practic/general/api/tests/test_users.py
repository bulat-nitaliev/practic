from rest_framework.test import APITestCase
from general.factories import UserFactory, CelFactory, CommentFactory
from rest_framework import status
from general.models import User

class UserTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory() 
        self.client.force_authenticate(user=self.user)
        self.url = '/api/users/'

    def test_users_me_structure(self):     
        cels = CelFactory.create_batch(5, author=self.user)
        
        expected_data = {
            "username": self.user.username,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "cels": [i.name for i in cels]
        }
        
        response = self.client.get(f'{self.url}me/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertDictEqual(response.data, expected_data)

    def test_user_registration(self):
        self.client.logout()
        data = {
            "username": "test_user_1",
            "password": "12345",
            "email": "test_user_1@gmail.com",
            "first_name": "John",
            "last_name": "Smith",
        }

        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_user = User.objects.last()