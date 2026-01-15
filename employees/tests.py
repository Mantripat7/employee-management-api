from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class EmployeeAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', password='test123'
        )
        token = self.client.post('/api/token/', {
            'username': 'test',
            'password': 'test123'
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_employee(self):
        response = self.client.post('/api/employees/', {
            'name': 'John',
            'email': 'john@test.com'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_email(self):
        self.client.post('/api/employees/', {
            'name': 'John',
            'email': 'john@test.com'
        })
        response = self.client.post('/api/employees/', {
            'name': 'Doe',
            'email': 'john@test.com'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
