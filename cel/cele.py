# Start it from hack directory using following command
# celery -A cel worker --app=cel.cele:app -l info
# celery -A cele worker --app=cele:app -l info
from celery import Celery

#app = Celery('tel', broker='redis://localhost:6379/0', include=['cel.tasks'])
app = Celery('tel', broker='redis://localhost:6379/0', include=['tasks'])