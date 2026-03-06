from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'name': 'Test User', 'email': 'test@example.com', 'team': 'marvel'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Add similar tests for Team, Activity, Leaderboard, Workout
