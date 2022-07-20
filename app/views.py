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
    def post(request):
        tokens.default_token_manager(
            client_id='e593930a-2cfb-424d-89c3-dc60e4620bf6',
            client_secret='tCCuItP6jsdhAOIrWiyLfB8EQ44Suzw6af6t7p2ck1tEkNpBTXFKkklOkQyCowoI',
            redirect_url="https://amo-connect.ru/api/v1/amo-test",
            storage=tokens.FileTokensStorage()
        )
        test = tokens.default_token_manager.init(
            code='def5020032ad60c2e36cc18c2ef03755fd8ddd35b23626026f286f59b27dccf7678010ec7513346deb54af57def2ac56a1f7dff990bcee173f281848f86111de5dcaa4b64be7f0675118668615b37e5e3c81426c767514189f3590f5d125a10d58a2bfa77009b3818ac8b45fe969a9bba60b83f0d4af578e9aea9778e714bdb95550cab3c3a2968efe1bb5795d8ce772b44712d1fbf83c25c5144282eb62879aa489491075dadec02b330af8c9139c889b39c03043a0b281455ccd35f8162f519a0e0d74633bf56c9d339f5ecc07824c7d2213019f5a38f5a27cbf0f51121247508d4df9242e784761777d9387af58c7230d83efe98f21bd22db347d4fa06e503667ae26603eff46456a2dcffdb5783aec34f7204a29fe50b057acf35cee12b10e39d4d3619bf8a48496bbe9355eedc3477bbe2ffc018010dbe0cf26254b237be4c9b3d65154de06b638c0debcb5df737f4d4a596e15bac5c172710fd7da15410b77a8d8e5dd9a5e125faa4cf48515d7c934038623767cc37af47e840dd43d54951ab869a5d131651f0f4cdf023ec42e1b70ef3b95d003c8079cbdbc3d4fa4b422ca03762a512bf6e4d19008055f5293635b640732080beae83a9e615da777cd1753bfcbd0859285351edb23ef38ec8b4cf2fce640ff52',
            skip_error=True
        )
        with open('results.txt', 'w') as file:
            file.write(test)
        return Response()
