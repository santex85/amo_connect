from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


# HbcGqxvFqH-e9M5xDY9BW-9z9ePFcSZMqzcewt9rW7cfcxPY9

class TestView(View):
    @staticmethod
    def get(request):
        return render(request, 'test/test.html', context={'name': 'alex'})


class GetInfoView(APIView):

    @staticmethod
    def post(request):
        # headers = {
        #     'X-Token': 'HbcGqxvFqH-e9M5xDY9BW-9z9ePFcSZMqzcewt9rW7cfcxPY9'
        # }
        # req = requests.get(
        #     f'https://online.bizon365.ru/api/v1/webinars/reports/get?webinarId=Uverennostidengi',
        #     headers=headers)
        # print(req.text)
        with open('test.txt', 'w') as file:
            file.write(str(request.data))
        return Response(status=status.HTTP_200_OK)
