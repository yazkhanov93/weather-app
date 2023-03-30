from django.contrib import admin
from .models import *


class DayInline(admin.StackedInline):
    model = Day
    extra = 1


class NightInline(admin.StackedInline):
    model = Night
    extra = 1


@admin.register(DailyForecast)
class DailyForecastAdmin(admin.ModelAdmin):
    list_display = ["date", "city","temp_min","temp_max","unit"]
    inlines = [DayInline, NightInline]


class DailyForecastInline(admin.StackedInline):
    model = DailyForecast
    extra = 0

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    inlines = [DailyForecastInline]
    list_display = ["name"]