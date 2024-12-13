from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .tasks import predict_yield

def simulate_crop(request):
    area = float(request.GET.get('area', 1))  # Área em hectares (valor padrão: 1 hectare)
    prediction = predict_yield(area)
    return JsonResponse({'area': area, 'predicted_yield': prediction})
