from tasks import app
import requests

@app.task
def get_agiliq():
    resp = requests.get("http://agiliq.com")
    return resp.status_code, resp.content[:50]