# Have another folder here called "cel". That works with two files
# This is another experimental file of trying to keep everything in a single file

from celery import Celery
import requests

app = Celery('cel_task', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

@app.task
def subtract(x, y):
    return x - y
