from rest_framework import serializers

from weather.models import *


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = "__all__"


class NightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Night
        fields = "__all__"


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class DailyForecastSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    night = serializers.SerializerMethodField()
    city = CitiesSerializer()
    class Meta:
        model = DailyForecast
        fields = "__all__"

    def get_day(self, obj):
        day = Day.objects.filter(day=obj)
        return DaySerializer(day, many=True).data

    def get_night(self, obj):
        night = Night.objects.filter(day=obj)
        return NightSerializer(night, many=True).data