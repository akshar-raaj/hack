# Used profiler
from profilehooks import profile
import requests
import time
#import re

class A(object):
    def __init__(self, url):
        self.url = 'http://agiliq.com'

    @profile
    def call_url(self):
        self.print_url()
        resp = requests.get(self.url)

    def print_url(self):
        print self.url
        self.another_url()
        for i in range(10):
            self.four()
        
    def another_url(self):
        print "another"
        time.sleep(1)
        self.two()

    def two(self):
        time.sleep(2)
        self.three()
        return 2

    def three(self):
        time.sleep(8)
        self.four()
        print 3

    def four(self):
        print 4
        


def hello(name):
    obj = A('http://agiliq.com')
    obj.call_url()
hello("akshar")

#profile.run('re.compile("hello|akshar")')
    
#profile.run('hello("akshar")')