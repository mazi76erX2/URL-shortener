from django.urls import path

from .views import CSRFGeneratorView, EncodeAPI, DecodeAPI


urlpatterns = [
    path('generate_csrf/', CSRFGeneratorView.as_view()),
    path('encode/', EncodeAPI, name='encode'),
    path('decode/', DecodeAPI, name='decode'),
]
