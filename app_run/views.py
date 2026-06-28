from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def company_details_view(request):
    return Response(
        {
            "company_name": "Кардио и Ко",
            "slogan": "До магазина — прогулка. Обратно — интервальная тренировка.",
            "contacts": "г. Пульсово, ул. 180 BPM, д. 60",
        },
        status=status.HTTP_200_OK
    )