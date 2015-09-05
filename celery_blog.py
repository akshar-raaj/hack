import requests
import time
import calendar
import pytz
import datetime
from celery import Celery
#from celery import Celery

#app = Celery('celery_blo', broker='redis://localhost:6379/0')
#app = Celery('celery_blog', broker='redis://localhost:6379/0')
from celery_config import app
from celery_add import add

@app.task(bind=True)
def fetch_url(self, url, current_num):
    print "**"
    print current_num
    print "**"
    current_num += 1
    resp = requests.get(url)
    #time.sleep(3)
    #print resp.status_code
    try:
        #if current_num <=1 :
        raise Exception()
    except Exception as exc:
        dt = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=1)
        # Converting dt to unix timestamp
        ts = calendar.timegm(dt.timetuple())
        dt = datetime.datetime.utcfromtimestamp(ts)
        raise self.retry(args=[url, current_num], eta=dt, exc=exc, max_retries=1)
        #raise self.retry(countdown=2, exc=exc, max_retries=3)
        #raise self.retry(args=[url, current_num], countdown=2, exc=exc, max_retries=3)
    return resp.status_code

def func(urls):
    current_num = 0
    for url in urls:
        fetch_url.delay(url, current_num)

urls = ["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"]

if __name__ == "__main__":
    func(urls)