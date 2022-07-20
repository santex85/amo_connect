from django.urls import path

from app.views import TestView, GetInfoView, TestAmoView

urlpatterns = [
    path('', TestView.as_view()),  # TODO сделать страницу заглушку
    path('api/v1/', GetInfoView.as_view()),
    path('api/v1/amo-test/', TestAmoView.as_view()),
]
