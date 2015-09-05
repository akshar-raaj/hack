from celery import Celery

#app = Celery('celery_config', broker='redis://localhost:6379/0', include=['celery_blog'])
app = Celery('celery_config', broker='redis://localhost:6379/0', include=['celery_blog', 'celery_add'])
#app = Celery('celery_config', broker='redis://localhost:6379/0', include=['pack.celery_fetch'])
app.config_from_object('celeryconfig')
