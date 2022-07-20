from django.urls import path

from app.views import TestView, GetInfoView

urlpatterns = [
    path('', TestView.as_view()),  # TODO сделать страницу заглушку
    path('api/v1/', GetInfoView.as_view())

]
