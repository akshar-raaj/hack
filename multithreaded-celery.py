# To check if adding multithreading to celery will make things faster.

from threading import Thread
from threading import Lock
import requests
from requests.exceptions import ConnectionError

urls = ["http://agiliq.com", "http://agiliq.com", "http://facebook.com", "http://youtube.com", "http://yahoo.com", "http://baidu.com", "http://amazon.com", "http://wikipedia.org", "http://taobao.com", "http://twitter.com"]
lock = Lock()

class UrlThread(Thread):

    def __init__(self, url):
        self.url = url
        super(UrlThread, self).__init__()

    def run(self):
        try:
            resp = requests.get(self.url)
            lock.acquire()
            print resp.status_code, self.url
            lock.release()
        except ConnectionError:
            print "Connection Error", self.url

threads = []
for url in urls:
    t = UrlThread(url)
    t.start()
    threads.append(t)

for t in threads:
    t.join()