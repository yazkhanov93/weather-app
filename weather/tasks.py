from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
import json
from .models import *
from apikey.models import *

@shared_task
# @periodic_task(run_every=timedelta(seconds=2), name="first_task")
def first_task():
    cityCode = City.objects.all().only("code")
    apikey = ApiKey.objects.latest("id")
    for i in cityCode:
        url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location}"
        url = url.format(location=i.code)
        params = {"apikey":apikey.key, "details":True, "metric":True}
        result = requests.get(url=url, params=params)
    
@shared_task
# @periodic_task(run_every=timedelta(seconds=3), name="second_task")
def second_task():
    print("second task")

