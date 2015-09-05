# Counts the number of words in a web page.
import requests

def count(url):
    r = requests.get(url)
    return len(r.text.split())