from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta


@shared_task
# @periodic_task(run_every=timedelta(seconds=2), name="first_task")
def first_task():
    print("this is first celery task")

@shared_task
# @periodic_task(run_every=timedelta(seconds=3), name="second_task")
def second_task():
    print("second task")