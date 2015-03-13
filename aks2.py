from redis import Redis # Redis will be used as a queue
from rq import Queue

q = Queue(connection=Redis()) # Tell this queue to talk with Redis to get the jobs

from aks1 import count

result = q.enqueue(count, "http://www.tcs.com")
print result
