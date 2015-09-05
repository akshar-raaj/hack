from celery import Celery
import requests
#import logging
import time

app = Celery('cel_task', broker='redis://localhost:6379/0')
#app = Celery('cel_task', broker='redis://54.69.176.94:6379/0')

#logger = logging.getLogger(__file__)
#logger.setLevel(logging.DEBUG)

#ch = logging.StreamHandler()
#formatter = logging.Formatter("%(name)s %(levelname)s %(message)s")
#ch.setFormatter(formatter)

#logger.addHandler(ch)

@app.task
def add(x, y):
    #logger.info("Adding %d and %d", x, y)
    time.sleep(2)
    print "celery task changed"
    print x+y
    return x + y

@app.task
def subtract(x, y):
    return x - y

@app.task
def fetch():
    resp = requests.get("http://agiliq.com")
    return resp.status_code