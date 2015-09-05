from .cele import app
import requests
import time
import logging

@app.task
def add(x, y):
    return x + y

@app.task
def get(url):
    time.sleep(5)
    resp = requests.get(url)
    return resp

add.delay(3, 4)
# add.apply_async([], {'x': 3, 'y': 4})
# add.apply_async(kwargs={'x': 2, 'y': 4})