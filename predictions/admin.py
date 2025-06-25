from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'prediction_score')