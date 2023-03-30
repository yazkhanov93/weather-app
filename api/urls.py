from django.urls import path
from api.weather.views import *


urlpatterns = [
    path("cities/", CityListView.as_view(), name="cities"),
    path("daily-forecast/", DailyForecastView.as_view(), name="daily-forecast"),
]