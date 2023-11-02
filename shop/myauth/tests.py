from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from django.utils.translation import gettext_lazy as _


class MyUserRegisterTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_data = {
            'username': 'testUser',
            'email': 'testUser@test.local',
            'full_name': 'Rest Test Testovich',
            'phone_number': 9213332233,
            'password1': 'Otus12345678',
            'password2': 'Otus12345678'
        }

        cls.user_data_same_email = {
            'username': 'testUser_same_email',
            'email': 'testUser@test.local',
            'full_name': 'Rest Test Testovich',
            'phone_number': 9213332233,
            'password1': 'Otus12345678',
            'password2': 'Otus12345678'
        }

        cls.user_broken_data = {
            'username': 'testUserBroken',
            'email': 'testUser@test.local',
            'full_name': 'Rest Test Testovich',
            'phone_number': 9213332233,
            'password1': 'Otus12389108',
            'password2': 'Otus12345678'
        }

    def test_success_register(self):
        response = self.client.post(
            reverse('myauth:register'),
            data=self.user_data
        )
        self.assertEqual(302, response.status_code)

        expected_username = self.user_data['username']
        created_user = get_user_model().objects.get(username=expected_username)

        self.assertEqual(expected_username, created_user.username)

    def test_failed_register(self):

        response = self.client.post(
            reverse('myauth:register'),
            data=self.user_broken_data
        )
        self.assertEqual(200, response.status_code)

        test_username = self.user_broken_data['username']

        try:
            get_user_model().objects.get(username=test_username)
        except ObjectDoesNotExist:
            pass

    def test_create_users_with_same_email(self):
        response_1 = self.client.post(
            reverse('myauth:register'),
            data=self.user_data
        )

        self.assertEqual(302, response_1.status_code)

        response_2 = self.client.post(
            reverse('myauth:register'),
            data=self.user_data_same_email
        )

        self.assertEqual(200, response_2.status_code)
