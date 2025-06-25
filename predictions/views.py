from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ml_model.services import PredictionService
from .serializers import PredictionInputSerializer, PredictionSerializer
from .models import Prediction


class PredictionAPIView(APIView):
    """
    Endpoint para realizar predicciones de adicción a redes sociales
    """

    def post(self, request):
        # Validar datos de entrada
        serializer = PredictionInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status': 'error',
                'message': 'Invalid input data',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        # Obtener servicio de predicción
        predictor = PredictionService()

        # Realizar predicción
        prediction_result = predictor.predict(serializer.validated_data)

        if prediction_result['status'] == 'error':
            return Response({
                'status': 'error',
                'message': prediction_result['message']
            }, status=status.HTTP_400_BAD_REQUEST)

        # Guardar predicción en base de datos
        prediction = Prediction.objects.create(
            input_data=serializer.validated_data,
            prediction_score=prediction_result['prediction']
        )

        # Retornar respuesta
        return Response({
            'status': 'success',
            'prediction': prediction_result['prediction'],
            'interpretation': prediction_result['interpretation'],
            'prediction_id': prediction.id
        }, status=status.HTTP_200_OK)