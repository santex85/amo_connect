import json

from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from amocrm.v2 import tokens


# HbcGqxvFqH-e9M5xDY9BW-9z9ePFcSZMqzcewt9rW7cfcxPY9

class TestView(View):
    @staticmethod
    def get(request):
        return render(request, 'test/test.html', context={'name': 'alex'})


class GetInfoView(APIView):

    @staticmethod
    def post(request):
        headers = {
            'X-Token': 'HbcGqxvFqH-e9M5xDY9BW-9z9ePFcSZMqzcewt9rW7cfcxPY9'  # TODO for prod move to settings
        }
        req = requests.get(
            f'https://online.bizon365.ru/api/v1/webinars/reports/getviewers?webinarId={request.data["webinarId"]}',
            headers=headers)
        users = json.loads(req.text)['viewers']
        for user in users:
            print(user)

        return Response(status=status.HTTP_200_OK)


class TestAmoView(APIView):

    @staticmethod
    def get(request):
        context = {
            'data': request.data
        }
        with open('results.txt', 'w') as file:
            file.write(str(request.data))
        return render(request, 'amo/redirect.html', context=context)

    @staticmethod
    def post(request):
        tokens.default_token_manager(
            client_id='0e31a2b6-c260-4f19-97fb-835b76c28579',
            client_secret='CsE4V9MVDtCp6WkIqGg5HaioZ5nNMyMRlDDK34ALxqZvyfBblqGgdKrkpPlHLLTc',
            subdomain='spliff',
            redirect_url="https://amo-connect.ru/api/v1/amo-test",
            storage=tokens.FileTokensStorage()
        )
        tokens.default_token_manager.init(
            code='def50200f245b39ae145da640e1d8ffa24f56bb4c01cc990d667e0ad05e37fe74ff02af87ec9fbbb5ab3b65bba12abfd0dd0c2228d6b012d2f71f31a2bcaf3d484daea6513c8a6587da40a90a0ab9920cd2762492e8dca043470a69f7771cae751e342ce9d91dd76a202abb75dc36e0c177c6093f0532a064ae9151406f1f7948d09c1174518980e03aca9859331924ca8efdce5695bdd41d46cb9a39ecce89e68423e8cb29fd0c20e469b9485365b23862997d2b71082cc006d3a62d9ea73a0b5ffe4c473c211b64385a95dec4b9497aa3191c09519359d4056f7dd91dc1a012b461770998ad05bc37ffaadbfe16492ac99a881273a67fb589ef86f18298e2e4da4a0b285ca1bb2cab1b071eb0c04bbf17371c336e25fcd5a7c96cf8db78fe2b47f62b089147b4b1ed44b924129e8b3aa355fd47b54a86348a8805d77bb91a2a06b80334f1bcece8d2925ba0515fd49e00e84fff40482ae2bbfc01fa6cd519d8cc9dc6b7b347e2a956fa874ac803bee787643d5887ea95571c7302c31d5c0820a0cbe9324be22a96dcfcfe28cef4d45299e27ca4cafcba31dad27272c6c099475782a3c83403c6753054f41bc8e1d76307da2a5aeb3c8e9533343b0561a38168d6ab74380da7d34ed8f1774f70bcc1a33ef3eba8a22e33ee0c8752170170e10717cc44bb40c490fe8aa',
            skip_error=True
        )
        return Response(status=status.HTTP_200_OK)
