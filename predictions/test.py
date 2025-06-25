from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Prediction


class PredictionAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_prediction_endpoint(self):
        test_data = {
            "Age": -1.18,
            "Gender": 0,
            "Academic_Level": 2,
            "Country": 10,
            "Avg_Daily_Usage_Hours": 0.22,
            "Most_Used_Platform": 1,
            "Affects_Academic_Performance": 1,
            "Sleep_Hours_Per_Night": -0.32,
            "Mental_Health_Score": -0.20,
            "Relationship_Status": 1,
            "Conflicts_Over_Social_Media": 0.15
        }

        response = self.client.post('/api/predict/', test_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('prediction', response.data)