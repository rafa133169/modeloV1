import joblib
import numpy as np
from django.conf import settings
from pathlib import Path


class PredictionService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_model()
        return cls._instance

    def load_model(self):
        """Carga el modelo entrenado desde el archivo .pkl"""
        model_path = Path(settings.BASE_DIR) / 'ml_model' / 'trained_model.pkl'
        self.model = joblib.load(model_path)
        print("Modelo cargado exitosamente!")  # Confirmación de carga

    def predict(self, input_data: dict) -> dict:
        """Realiza predicciones con los datos de entrada"""
        try:
            # Preprocesamiento de entrada
            features = np.array([
                float(input_data['Age']),
                int(input_data['Gender']),
                int(input_data['Academic_Level']),
                int(input_data['Country']),
                float(input_data['Avg_Daily_Usage_Hours']),
                int(input_data['Most_Used_Platform']),
                int(input_data['Affects_Academic_Performance']),
                float(input_data['Sleep_Hours_Per_Night']),
                float(input_data['Mental_Health_Score']),
                int(input_data['Relationship_Status']),
                float(input_data['Conflicts_Over_Social_Media'])
            ]).reshape(1, -1)

            # Predicción
            prediction = float(self.model.predict(features)[0])

            return {
                'status': 'success',
                'prediction': prediction,
                'interpretation': self._interpret_prediction(prediction)
            }

        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

    def _interpret_prediction(self, score: float) -> str:
        """Interpreta el score de adicción"""
        if score < -1.5:
            return "Bajo riesgo de adicción"
        elif -1.5 <= score < 1.5:
            return "Riesgo moderado"
        else:
            return "Alto riesgo de adicción"


# Singleton para usar en todo el proyecto
prediction_service = PredictionService()