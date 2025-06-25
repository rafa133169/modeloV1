from django.db import models

class Prediction(models.Model):
    input_data = models.JSONField()
    prediction_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id} - Score: {self.prediction_score}"