from celery import Celery
import requests

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y, name):
    return x+y, name

@app.task
def get():
    resp = requests.get("http://agiliq.com")
    return resp.status_code, resp.content[:50]