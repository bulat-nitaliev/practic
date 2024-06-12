from rest_framework.test import APITestCase
from general.factories import UserFactory, CelFactory, CommentFactory
from rest_framework import status
from general.models import  Comment

class CommentTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = '/api/comment/'

    def test_create_comment(self):
        cel = CelFactory(author=self.user)
        data = {"body": "New Comment", "cel": cel.pk}

        response = self.client.post(self.url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['body'], data['body'])
        cel.refresh_from_db()
        comment = Comment.objects.last().body
        cel_comment = cel.comments.last().body

        self.assertEqual(data['body'], comment)
        self.assertEqual(cel_comment, comment)

    def test_create_comment_not_main_cel(self):
        cel = CelFactory()
        data = {"body": "New Comment", "cel": cel.pk}

        response = self.client.post(self.url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Comment.objects.all().count(), 0)
        self.assertEqual(response.data['detail'], 'Вы не можете добавить коментарий к чужой цели')
