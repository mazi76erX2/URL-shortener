from rest_framework import serializers
from .models import Url


class UrlEncodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = (
            'original_url',
        )


class UrlDecodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = (
            'shortened_url',
        )
