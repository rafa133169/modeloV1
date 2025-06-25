from rest_framework import serializers
from .models import Prediction

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

class PredictionInputSerializer(serializers.Serializer):
    Age = serializers.FloatField()
    Gender = serializers.IntegerField()
    Academic_Level = serializers.IntegerField()
    Country = serializers.IntegerField()
    Avg_Daily_Usage_Hours = serializers.FloatField()
    Most_Used_Platform = serializers.IntegerField()
    Affects_Academic_Performance = serializers.IntegerField()
    Sleep_Hours_Per_Night = serializers.FloatField()
    Mental_Health_Score = serializers.FloatField()
    Relationship_Status = serializers.IntegerField()
    Conflicts_Over_Social_Media = serializers.FloatField()