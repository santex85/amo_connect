from django.urls import path

from app.views import TestView

urlpatterns = [
    path('', TestView.as_view()),
]
