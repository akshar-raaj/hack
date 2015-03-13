import requests

def count(url):
    r = requests.get(url)
    return len(r.text.split())