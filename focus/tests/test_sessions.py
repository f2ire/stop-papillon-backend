from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class FocusSessionAPITest(APITestCase):
    def setUp(self):
            self.user = get_user_model().objects.create_user(username= "testuser", password= "testpass")
            self.client.force_authenticate(user=self.user)

    def test_create_focus_session(self):
        
        url = reverse('session-list')  # adapte ce nom
        data = {
            "expected_duration": 45,
            "was_successful": True,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_focus_session_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('session-list')  # adapte ce nom
        data = {
            "expected_duration": 45,
            "was_successful": True,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)