from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from weather.models import *


class CityListView(APIView):
    def get(self, request):
        try:
            cities = City.objects.all()
            serializer = CitiesSerializer(cities, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DailyForecastView(APIView):
    def get(self, request):
        try:
            city_code = request.query_params.get("city_code", None)
            daily_forecast = DailyForecast.objects.filter(city=city_code)
            serializer = DailyForecastSerializer(daily_forecast, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)