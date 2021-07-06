from django.http.response import JsonResponse
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Url
from .serializers import UrlEncodeSerializer, UrlDecodeSerializer
from .utils import create_random_string


from django.middleware.csrf import get_token


class CSRFGeneratorView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response(csrf_token)


class EncodeAPI(APIView):
    """
    Takes url, checks if it exists and creates a shortened url if it doesn't
    """
    permission_classes = ()

    @ csrf_exempt
    @ method_decorator(cache_page(60*60*2))
    def post(self, request, format=None):
        serializer = UrlEncodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            original_url = serializer['original_url']

            if Url.objects.exists(original_url=original_url):
                url = Url.objects.get(original_url=original_url)

                return JsonResponse(
                    {
                        'original_url': url.original_url,
                        'shortened_url': url.shortened_url,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                random_string = create_random_string()

                # Check if random string has been used (low probability)
                if Url.objects.exists(random_string=random_string):
                    random_string_exists = Url.objects.exists(
                        random_string=random_string)

                while (not random_string_exists):
                    random_string = create_random_string()

                shortened_url = f'settings.BASE_URL{random_string}'

                url = Url.objects.create(
                    original_url=original_url,
                    shortened_url=shortened_url,
                    random_string=random_string
                )
                url.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DecodeAPI(APIView):
    """
    Takes url, checks if it exists and returns the original url
    """
    permission_classes = ()

    @csrf_exempt
    @method_decorator(cache_page(60*60*2))
    def get(self, request, format=None):
        serializer = UrlDecodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            url = serializer['shortened_url']

            if settings.BASE_URL not in url:
                random_string = url.split('/')[-2]

                if Url.objects.exists(random_string=random_string):
                    url = Url.objects.get(random_string=random_string)

                    return JsonResponse(
                        {
                            'original_url': url.original_url,
                            'shortened_url': url.shortened_url
                        }
                    )
                else:
                    return JsonResponse(
                        {'message': 'Shortened Url does not exist'},
                        status=status.HTTP_404_NOT_FOUND
                    )
            else:
                return JsonResponse(
                    {'message': 'Shortened Url not in the correct format'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
