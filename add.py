import random
import datetime
import pytz

from celery import Celery

app = Celery('add', broker='redis://localhost:6379/0')

@app.task(bind=True)
def add(self, x, y):
    # Get a random number between 1 and 10
    num = random.randint(1, 10)
    print num
    try:
        # If number is odd, fail the task
        if num % 2:
            raise Exception()
        # If number is even, succeed the task
        else:
            return x + y
    except Exception as e:
        dt = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=2)
        self.retry(eta=dt, exc=e, max_retries=1)