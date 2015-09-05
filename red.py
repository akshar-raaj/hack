# Trying redis python client
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age